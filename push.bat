REM TODO: switch branch, and markdown and add to gh-pages
@echo off
if NOT [%1]==[] (
    git commit -am%1
    git push
    )