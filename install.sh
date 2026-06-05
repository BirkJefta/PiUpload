#!/bin/bash
# install.sh 

echo "[*] installing dependencies..."

sudo apt-get update
sudo apt-get install -y python3-pip python3-requests

mkdir -p /home/pi/Desktop/PiUpload
cp upload.py /home/pi/Desktop/PiUpload/
cp 99-track-upload /etc/NetworkManager/dispatcher.d/

# make scripts executable
chmod +x /home/pi/Desktop/PiUpload/upload.py
chmod +x /etc/NetworkManager/dispatcher.d/99-track-upload

#cron job for upload.py every hour if Wi-Fi is 
(crontab -l 2>/dev/null; echo "0 * * * * /usr/bin/python3 /home/pi/Desktop/PiUpload/upload.py") | crontab -

echo "Installation complete."