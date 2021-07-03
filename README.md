About
-----

This repo hold the server config for maps like [jochenklar/berlin-maps](https://github.com/jochenklar/berlin-maps) an others.


Setup
-----

```bash
apt-get install tilestache gunicorn3
```

or

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install gdal==2.4.4
pip install -r requirements.txt
```

Usage
-----

```bash
# run dev server
tilestache-server -c config.json

# seed tiles
tilestache-seed -c config.json -b 55.05 5.86 47.27 14.04 -l bbs 10
```
