#!/usr/bin/env python

'''
This module is called as a script after installation of thywill in order to run necessary setup tasks.
'''

import sys
import thywill_server.settings as settings

paths = []
paths.append(settings.THYWILL_ROOT +'/thywill_server/src/')
paths.append(settings.THYWILL_ROOT +'/thywill_apps/src/')
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
        
        
#--------------------------------------------------------------------
# Django setup
#--------------------------------------------------------------------

from thywill_server.client_interface.client_interface_component import ClientInterfaceComponent
from thywill_server.client_interface.django.component import DjangoComponent

client_interface_component = ClientInterfaceComponent.factory()
if isinstance(client_interface_component, DjangoComponent):
    from django.core import management
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'thywill_server.client_interface.django.settings'
    management.call_command('syncdb')