'''
The thywill_server package contains:

1) the glue code to manage interactions between the various components of the server side of thywill, most of which are third party applications.

2) the functional code to manage thywill processes and data: state, actions, reactions, and so forth.
'''

import os
import sys
sys.path.insert(0, os.path.split(__file__)[0])

# Not really deserving of a version number.
__version__ = (0, 0, 1)