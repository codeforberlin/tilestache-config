Setup
-----

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Usage
-----

```bash
# run dev server
tilestache-server.py -c config.json

# seed tiles
tilestache-seed.py -c config.json -b 55.05 5.86 47.27 14.04 -l bbs 10
```
