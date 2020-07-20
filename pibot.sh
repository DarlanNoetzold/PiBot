#!/bin/bash
cd ~/mjpg-streamer


if pgrep mjpg_streamer > /dev/null
then
	echo "mjpg-streamer already running!"
else
	mjpg_streamer  -o "output_http.so -w ./www" -i "input_raspicam.so -vf" & 
	echo "mjpg-streamer started"

fi
sleep 2
echo "Inicializando o PiBOT !"
sleep 1
cd ~/pibot
python3 pibot-web.py
