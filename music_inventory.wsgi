
#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/music_inventory/")

from catalog import app as application
application.secret_key = '7836nZbsdjhsadbasgd6qvZH'
