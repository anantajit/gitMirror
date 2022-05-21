SCRIPT_DIRECTORY="$(pwd)"
cd $1
git push github
cd $SCRIPT_DIRECTORY
