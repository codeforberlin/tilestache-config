#!/usr/bin/env python
import argparse
import json
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--layer', default=None)

args = parser.parse_args()

with open('config.json') as fp:
    config = json.load(fp)

for layer in config['layers']:
    if args.layer in [None, layer]:
        for zoom in ['10', '11', '12', '13']:
            cmd = ['tilestache-seed', '-c', 'config.json', '-l', layer,
                   '-b', '52.68', '13.07', '52.33', '13.77', zoom]
            subprocess.check_call(cmd)
