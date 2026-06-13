#!/bin/bash

#checks for Wi-Fi connection and runs upload.py when connected

INTERFACE=$1
ACTION=$2

case "$ACTION" in
    up)
        if [ "$INTERFACE" = "wlan0" ]; then
            /usr/bin/python3 /home/user/Desktop/PiUpload/upload.py
        fi
        ;;
esac