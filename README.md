Setup
-----

```bash
apt-get install tilestache gunicorn3
```

Usage
-----

```bash
# run dev server
tilestache-server -c config.json

# seed tiles
tilestache-seed -c config.json -b 55.05 5.86 47.27 14.04 -l bbs 10
```
