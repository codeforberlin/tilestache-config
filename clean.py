#!/usr/bin/env python
import argparse
import json
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--layer', default=None)

args = parser.parse_args()

with open('config.json') as fp:
    config = json.load(fp)

base_path = Path('tmp')

for layer in config['layers']:
    if args.layer in [None, layer]:
        for zoom in ['16', '17', '18', '19', '20']:
            path = base_path / layer / zoom
            print(path)

            try:
                shutil.rmtree(path)
            except FileNotFoundError:
                pass
