"""Invoke is cross-platform task automation for Windows, similar to C 'make'.

This project workflow:

    `inv --list` - refresh available commands
    make changes in source files
    `inv html` - builds html files locally from markdown source
    `inv show` - display local version of the web site in browser
    `inv push <message>` - publish website to github pages
    commit changes in source files to different repo.

This invoke file is based on tasks.py from:

    https://github.com/mini-kep/parser-rosstat-kep/blob/dev/tasks.py

Original advice about Windows workaround for invoke:

    https://github.com/pyinvoke/invoke/issues/371#issuecomment-259711426

Intended to adopt best practice:

    https://github.com/pyinvoke/invocations

"""
import sys
import os
import shutil
from pathlib import Path

from invoke import Collection, task

GH_PAGES_FOLDER = "gh-pages"


def remove(path):
    if os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def wipe_folder(folder, exclude=[".git", ".nojekyll"]):
    for path in os.listdir(folder):
        if path not in exclude:
            fullpath = os.path.join(folder, path)            
            remove(fullpath)
            print("Deleted", fullpath)


def run(ctx, cmd):
    return ctx.run(cmd, hide=False, warn=True)


def run_all(ctx, commands):
    cmd = " && ".join(commands)
    return run(ctx, cmd)


@task
def clean(ctx):
    """Wipe html documentation. Sometimes you need this to restart a build."""
    wipe_folder(GH_PAGES_FOLDER)


@task
def html(ctx):
    """Build html documentation with `sphinx-build`.
       Same as `sphinx-build -b html docs gh-pages -c .`"""
    # WONTFIX: console output is colorless, errors do not show in red
    run(ctx, f"sphinx-build -b html docs {GH_PAGES_FOLDER} -c .")


@task
def pdf(ctx):
    """Make a pdf file of the documentation (not implemented)."""
    pass


def quote(s: str) -> str:
    return '"' + s + '"'


# create branch + https://gist.github.com/cobyism/4730490#gistcomment-2375522
# see also https://webapps.stackexchange.com/a/103336/216781
# and
# https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase
@task
def push(ctx, message="Deploy to gh-pages"):
    """Push site content to Github Pages. Use `html` command to build content."""
    commands = [f"cd {GH_PAGES_FOLDER}",
                "git add --all",
                # git commit -m "Deploy to gh-pages"
                "git commit -m%s" % quote(message),
                "git push origin gh-pages",  # remote must be set
                "cd .."]
    run_all(ctx, commands)


@task
def show(ctx):
    """Show local documentation in default browser."""
    run(ctx, f"start {GH_PAGES_FOLDER}/index.html")


@task
def help(ctx):
    """Print this extended doctsring at console."""    
    run(ctx, "invoke --list")
    print()
    print(__doc__)


ns = Collection()
for t in [clean, html, show, push, pdf, help]:
    ns.add_task(t)


# Workaround for Windows execution
if sys.platform == 'win32':
    # This is path to cmd.exe
    ns.configure({'run': {'shell': os.environ['COMSPEC']}})
