'''
A trivial Application Interface for an application consisting of Python code running as 
a part of this process. 

That code must be a Python package, and must contain a module "thywill_interface.py" 
that implements the following functions:

----------

def message_from_client(uuid, raw_message):
    
    # notify your application and do something
    
    return
    
def send_message_to_client(uuid, raw_message):

    # possibly do some other things, but definitely do this one thing:

    ApplicationInterfaceComponent.factory().send_message_to_client(uuid, raw_message);
    
    
def configure_client(uuid, client_configuration):

    # do something, such as whatever setup is needed for a newly arrived client, and
    # add appropriate values and resources to the client_configuration object

    # e.g. from the proof of concept test application:
    client_configuration.set_application_parameter('apps_static_path', APPS_STATIC_PATH)
    client_configuration.set_application_resource({
        'type': 'javascript',
        'resource': APPS_STATIC_PATH + '/test/proof_of_concept/proof_of_concept.js',
    })

----------

For simple examples of how this works in practice, look at the thywill_apps packages.

'''