import os

import TileStache

config = os.path.join(os.path.dirname(__file__), 'tilestache.cfg')
application = TileStache.WSGITileServer(config)
