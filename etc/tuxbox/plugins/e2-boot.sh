#!/bin/sh

# start enigma2
if [ -e /usr/bin/enigma2 ]; then
	wget -q -O - http://127.0.0.1:80/control/message?popup="enigma2 will start after rebooting..." > /dev/null

	rm -rf /etc/.nhd2
	touch /etc/.e2

fi
reboot

exit 0
