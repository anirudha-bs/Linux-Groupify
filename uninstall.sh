#!/bin/sh

if [ `whoami` != 'root' ]
then
echo "This script must be run as root."
exit 1;
fi
echo "Uninstalling Groupify...."
sudo rm /usr/local/bin/groupify && sudo rm /usr/share/applications/groupify.desktop && sudo rm /usr/share/pixmaps/groupify.png && sudo rm /usr/share/pixmaps/folder_icon.png
if [ $? -eq 0 ]
then
echo "Uninstall complete."
else
echo "Error deleting files, no files found or permissions denied"
fi

