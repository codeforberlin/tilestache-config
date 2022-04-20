About
-----

This repo hold the server config for maps like [jochenklar/berlin-maps](https://github.com/jochenklar/berlin-maps) an others.


Setup
-----

```bash
apt-get install tilestache gunicorn memcached python-requests python-gdal gdal-bin
```

Usage
-----

```bash
# run dev server
tilestache-server -c config.json

# seed tiles
tilestache-seed -c config.json -b 55.05 5.86 47.27 14.04 -l bbs 10
```

Advanced
--------

Tilestache can also be installed using `pip`, but it will work only with `TileStache==1.51.4` and Python 2.

GDAL can be build manually, but it should be `<=2.4.4`. Then, the Python bindings need to be installed using `GDAL==2.4.4` (the version must match).

If GDAL is installed with a `--prefix`, e.g. `/opt/gdal-2.4.4`, the following command needs to be used to start the server:

```bash
PATH=/opt/gdal-2.4.4/bin:$PATH LD_LIBRARY_PATH=/opt/gdal-2.4.4/lib tilestache-server -c config.json
```
