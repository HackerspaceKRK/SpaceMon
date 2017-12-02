__version__ = 1.0
__cacheable__ = True

import urllib2
import json
import time
from application import config


CONFIG_KEY = 'module_mqtt2json_open'

def update_document(data):
	remote = urllib2.urlopen(config.get(CONFIG_KEY, 'url'), timeout=config.getint(CONFIG_KEY, 'timeout')).read()
	remote = json.loads(remote)

	if remote['zm/hs_active']['timestamp'] < time.time() - 120:
		return

	is_open = remote['zm/hs_active']['payload'] == 1
	
	if not data.get('sensors'):
		data['sensors'] = {}

		if not data.get('state'):
			data['state'] = {}

		data['state']['open'] = is_open

