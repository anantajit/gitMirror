git clone $1 $2 # this is just a wrapper for git clone where we specify two arguments
SCRIPT_DIRECTORY="$(pwd)"
cd $2
git remote add github $3 # this is the push location for the repo
git branch -M master
git push -u github master
cd $SCRIPT_DIRECTORY
