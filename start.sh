#!/usr/bin/env bash

cd ~/tv-remote/ && venv/bin/python3 -m tvserver >>~/.tvserver.log 2>&1
