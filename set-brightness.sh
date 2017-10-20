#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
	echo "Usage: set-brightness.sh [0-255]"
	exit 1
fi

echo -n 'Backlight power [0=on]:  '
echo    0    | sudo tee /sys/class/backlight/rpi_backlight/bl_power

echo -n 'Backlight level [0-255]: '
echo    "$1" | sudo tee /sys/class/backlight/rpi_backlight/brightness
