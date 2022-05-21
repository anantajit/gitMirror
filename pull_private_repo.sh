SCRIPT_DIRECTORY="$(pwd)"
cd $1
git pull origin master
cd $SCRIPT_DIRECTORY
