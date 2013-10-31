#!/bin/sh
#DESCRIPTION=This script will delete all crash-logs from /media/hdd/logs/ and /home/root/logs/
rm -rf /media/hdd/logs/enigma2_crash*
rm -rf /media/hdd/enigma2_crash*
rm -rf /home/root/logs/enigma2_crash*
echo ""
exit 0
