"""Task automation for Windows using python invoke, similar to 'make'

Workflow:

    inv html - builds html files from markdown source 
    inv show - display local version of the web site
    inv push <message> - publish website to github pages

Based on tasks.py from:

    https://github.com/mini-kep/parser-rosstat-kep/blob/dev/tasks.py

Original advice about Windows workaround for invoke:
    
    https://github.com/pyinvoke/invoke/issues/371#issuecomment-259711426

"""
import sys
import os
import shutil
from pathlib import Path

from invoke import Collection, task

def remove(path):
    if os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path): 
        shutil.rmtree(path)


def remove_folder(folder, exclude = [".git", ".nojekyll"]):
    for path in os.listdir(folder):
        if path not in exclude:
            fullpath = os.path.join(folder, path)
            print("Deleting:", fullpath)
            remove(fullpath)


def run(ctx, cmd):
    return ctx.run(cmd, hide=False, warn=True) 


def run_all(ctx, commands):
    cmd = " && ".join(commands)
    return run(ctx, cmd)


@task
def clean(ctx):
    """Wipe html documentation"""
    remove_folder("gh-pages")


@task
def ls(ctx):
    """List current directory"""
    run(ctx, "dir /b")


@task
def html(ctx):
    """Build html documentation with `sphinx-build`"""
    # WONT FIX: console output is colorless
    run(ctx, "sphinx-build -b html docs gh-pages -c .")


@task
def pdf(ctx):
    pass


def quote(s):
    return f'"{s}"'


@task
def push(ctx, message="build html"):
    """Build html documentation"""
    commands = ["cd gh-pages", 
                #"git add .", 
                "git commit -am%s" % quote(message),
                "git push",
                "cd .."]
    run_all(ctx, commands)

# fixme: errors in VSCode
@task
def show(ctx):
    """Show documentation in default browser."""
    run(ctx, "start gh-pages/index.html")


@task
def help(ctx):
    """Print this file doctsring at console."""
    print (__doc__)
    

ns = Collection()
for t in [ls, clean, html, show, push, pdf, help]: 
   ns.add_task(t)


# Workaround for Windows execution
if sys.platform == 'win32':
    # This is path to cmd.exe
    ns.configure({'run': {'shell': os.environ['COMSPEC']}})

