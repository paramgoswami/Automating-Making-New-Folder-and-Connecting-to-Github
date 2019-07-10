@ECHO OFF
SET /P uname=Please enter your project name: 
cd C:\Users\param\Desktop\Projects\Github 
python create.py %uname%
cd C:\Users\param\Desktop\Projects\%uname% 
echo C:\Users\param\Desktop\Projects\%uname%
git init
git remote add origin https://github.com/paramgoswami/%uname%.git
ECHO >> README.md
git add .
git commit -m "Initial Commit. Added an empty Readme"
git push -u origin master
code .
:End