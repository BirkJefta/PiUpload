#!/bin/bash
# install.sh 

echo "[*] Installing dependencies..."

sudo apt-get update
sudo apt-get install -y python3-pip python3-requests


mkdir -p /home/user/Desktop/PiUpload
cp upload.py /home/user/Desktop/PiUpload/
cp 99-track-upload /etc/NetworkManager/dispatcher.d/


chmod +x /home/user/Desktop/PiUpload/upload.py
sudo chmod +x /etc/NetworkManager/dispatcher.d/99-track-upload


(crontab -l 2>/dev/null; echo "0 * * * * /usr/bin/python3 /home/user/Desktop/PiUpload/upload.py") | crontab -

echo "Installation complete."