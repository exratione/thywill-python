'''
Interface to thywill.
'''
from thywill_server.application_interface.application_interface_component import ApplicationInterfaceComponent
from thywill_apps.settings import APPS_STATIC_PATH

def message_from_client(uuid, raw_message):
    '''
    Take action in response to a message from a client.
    
    :Parameters:
        - uuid: a string ID for this client
        - raw_message: the message to be sent    
    '''
    
    # What we're going to do here is turn the message right around and send it back
    # to the client who sent it.
    send_message_to_client(uuid, raw_message)
    
def send_message_to_client(uuid, raw_message):
    '''
    Send a message on to the client via the Application Interface.
    
    :Parameters:
        - uuid: a string ID for this client
        - raw_message: the message to be sent
    '''
    ApplicationInterfaceComponent.factory().send_message_to_client(uuid, raw_message);
    
    
def _bootstrap_client(uuid, client_configuration):
    '''
    Take the necessary actions for a new client, such as adding application parameters and resources 
    to the client configuration object.
        
    :Parameters:
        - uuid: a string ID for this client
        - client_configuration: a ClientConfiguration object.
    ''' 
    client_configuration.set_application_parameter('title', 'Test: Proof of Concept')
    client_configuration.set_application_parameter('apps_static_path', APPS_STATIC_PATH)
    client_configuration.add_application_resource({
        'type': 'javascript',
        'resource': APPS_STATIC_PATH + '/test/proof_of_concept/proof_of_concept.js',
    })