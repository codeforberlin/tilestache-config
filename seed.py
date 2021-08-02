#!/usr/bin/env python3
import json
import subprocess

with open('config.json') as fp:
    config = json.load(fp)

for layer in config['layers']:
    for zoom in ['10', '11', '12', '13']:
        cmd = ['tilestache-seed', '-c', 'config.json', '-l', layer,
               '-b', '52.68', '13.07', '52.33', '13.77', zoom]
        subprocess.check_call(cmd)
