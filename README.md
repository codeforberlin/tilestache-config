About
-----

This repo hold the server config for maps like [jochenklar/berlin-maps](https://github.com/jochenklar/berlin-maps) an others.

Other projects
-----

* [luftbilder.berlin.codefor.de](https://luftbilder.berlin.codefor.de) showcases areal images from differnt years [Github](https://github.com/codeforberlin/luftbilder.berlin.codefor.de) 
* [maps.berlin.codefor.de](https://maps.berlin.codefor.de) showcases all kind of maps [Github](https://github.com/codeforberlin/maps.berlin.codefor.de) 
<!-- * [github.com/codeforberlin/tilestache-config](https://github.com/codeforberlin/tilestache-config) is the config for serving areal imagery from file ([config](https://github.com/codeforberlin/tilestache-config/blob/master/config.json)) -->
* [github.com/codeforberlin/mapproxy-config](https://github.com/codeforberlin/mapproxy-config) is a map proxy for some imagery layers by the City of Berlin

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
