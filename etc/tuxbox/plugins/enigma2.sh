#!/bin/sh

# start enigma2
if [ -e /usr/bin/enigma2 ]; then
	wget -q -O - http://127.0.0.1:80/control/message?popup="enigma2 will start..." > /dev/null
	sleep 4
	killall -9 neutrino
	enigma2
fi


exit 0
