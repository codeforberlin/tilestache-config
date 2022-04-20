#!/usr/bin/env python
import json
import shutil
from pathlib import Path

with open('config.json') as fp:
    config = json.load(fp)

base_path = Path('tmp')

for layer in config['layers']:
    for zoom in ['16', '17', '18', '19', '20']:
        path = base_path / layer / zoom
        print(path)

        try:
            shutil.rmtree(path)
        except FileNotFoundError:
            pass
