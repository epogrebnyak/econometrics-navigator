@echo off
if [%1]==[] goto end

cd gh-pages 
git add . 
git commit -am%1
git push
cd ..
	
: end	