#!/usr/bin/env bash

if [ "$#" -eq 0 ]; then
	echo "Usage: $0 <command-to-send-to-cec-client>"
	echo "Example: $0 tx 10:82:10:00"
	exit 1
fi

echo "echo '$*' | cec-client RPI --single-command --log-level 1"
echo "$*" | cec-client RPI --single-command --log-level 1
