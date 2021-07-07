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
