'''
Core settings for thywill. The components used are defined and provided with their configuration settings.
'''

# TODO: obtain settings from elsewhere; e.g. file, database.

# Where is the thywill_server folder located?
THYWILL_ROOT = '/var/www/thywill-python'

THYWILL_HOST = '184.73.179.223'

THYWILL_CONFIG = {
                  
    # handles bootstrapping, API for communication to the client
    'client_interface': {
        'component': 'django',
        'static_path': '/static',
        'template_path': THYWILL_ROOT + '/thywill_server/django_static/templates',
        'port': 443,
        'secure': True,
        'hostname': THYWILL_HOST,
        'secret_key': 'n#)+35bs3w_z1p(4mdtss+$4iolmyg793rvhiwvm=&q)07k@%^',
    },
    
    # component that pushes messages out to the client
    'push': {
        'component': 'orbited stomp',
        'orbited_static_path': '/s',
        'orbited_port': 8443,
        'orbited_secure': True,
        'orbited_hostname': THYWILL_HOST, 
        'stomp_port': 61613,
        'stomp_hostname': 'localhost', # both the client and server will be using this configuration parameter
    },
    
    # database component
    'database': {
        'component': 'mysql',
        'database': 'thywill',
        'user': 'thywill',
        'password': 'dummy_password',
        'host': 'localhost',
        'port': 3306,
    },
    
    # logging component
    'log': {
        'component': 'file',
        'path': '/var/log/thywill',
        'level': 'debug',
    },
    
    # an interface to the running application that uses thywill
    'application_interface': {
        'component': 'local_python',
        'application_package': 'thywill_apps.test.proof_of_concept'
    },
    
}
