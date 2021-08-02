#!/usr/bin/env python3
import json
import subprocess

with open('config.json') as fp:
    config = json.load(fp)

for layer in config['layers']:
    for zoom in ['10', '11', '12', '13']:
        cmd = ['tilestache-seed', '-c', 'config.json',
               '-b', '52.55', '13.28', '52.46', '13.51',
               '-l', layer, zoom]
        subprocess.check_call(cmd)
