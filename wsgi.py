import os

import TileStache

config = os.path.join(os.path.dirname(__file__), 'config.json')
application = TileStache.WSGITileServer(config)
