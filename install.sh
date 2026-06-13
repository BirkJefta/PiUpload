#!/bin/bash
# install.sh - Den rene version


sudo apt-get update
sudo apt-get install -y python3-pip python3-requests

INSTALL_DIR="/home/user/PiUpload"
mkdir -p $INSTALL_DIR

cp upload.py $INSTALL_DIR/
cp 99-track-upload /etc/NetworkManager/dispatcher.d/

sudo chmod +x /etc/NetworkManager/dispatcher.d/99-track-upload

(crontab -l 2>/dev/null; echo "0 * * * * /usr/bin/python3 $INSTALL_DIR/upload.py") | crontab -

echo "Installation complete in $INSTALL_DIR"