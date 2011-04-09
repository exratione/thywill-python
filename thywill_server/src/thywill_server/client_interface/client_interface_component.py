
from thywill_server.component import Component
from thywill_server.settings import THYWILL_CONFIG

class ClientInterfaceComponent(Component):
    '''
    The parent class for web server component definitions.
    '''
    singleton = None
    
    @staticmethod
    def factory():
        '''Get the data_store component object.'''
        if not ClientInterfaceComponent.singleton:
            if THYWILL_CONFIG['client_interface']['component'] == 'django':
                from thywill_server.client_interface.django.component import DjangoComponent
                ClientInterfaceComponent.singleton = DjangoComponent(THYWILL_CONFIG['client_interface']);
            else:
                raise NotImplementedError('No implementation for client_interface = ' + THYWILL_CONFIG['client_interface']['component'])   
        return ClientInterfaceComponent.singleton 

    def __init__(self, config):
        '''
        Constructor.
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        raise NotImplementedError()
    
    def create_client_configuration(self, uuid):
        '''
        Return information to pass to the client so it can configure its expectations accordingly.
        This is built from the input of various components in the thywill system, and the provided
        additional_parameters.
        
        :Parameters:
            - uuid: a string ID for this client
            
        :Return:
            ClientConfiguration
        '''  
        raise NotImplementedError()
        