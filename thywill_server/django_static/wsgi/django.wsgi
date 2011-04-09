import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'thywill_server.client_interface.django.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Add the thywill paths. Adjust appropriately if you are installing to a different location.
paths = []
paths.append('/var/www/thywill/thywill_server/src/')
paths.append('/var/www/thywill/thywill_apps/src/')
for path in paths:
	if path not in sys.path:
		sys.path.append(path)