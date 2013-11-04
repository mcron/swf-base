#!/bin/sh

# start enigma2
wget -q -O - http://127.0.0.1:80/control/message?popup="enigma2 will start..." > /dev/null
sleep 5
killall -9 neutrino
init 3

exit 0
