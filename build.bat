REM sphinx-build -b html source docs -c .

if NOT [%1]==[] (
    git commit -am%1
    git push
    )