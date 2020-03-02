#!/bin/sh

if [ `whoami` != 'root' ]
then
echo "This script must be run as root."
exit 1;
fi
echo "Installing Groupify...."
pwd=$(pwd)
sudo mv $pwd/dist/groupify /usr/local/bin && sudo mv $pwd/groupify.desktop /usr/share/applications && sudo mv groupify.png /usr/share/pixmaps && mv folder_icon.png /usr/share/pixmaps
if [ $? -eq 0 ]
then
echo "Moved files"
echo "Installation complete."
else
echo "Error moving files to bin or permissions denied"
fi

