
from thywill_server.component import Component
from thywill_server.settings import THYWILL_CONFIG

class ApplicationInterfaceComponent(Component):
    '''
    The parent class for application interface component definitions.
    '''
    singleton = None
    
    @staticmethod
    def factory():
        '''Get the application_interface component object.'''
        if not ApplicationInterfaceComponent.singleton:
            if THYWILL_CONFIG['application_interface']['component'] == 'local_python':
                from thywill_server.application_interface.local_python.component import LocalPythonComponent
                ApplicationInterfaceComponent.singleton = LocalPythonComponent(THYWILL_CONFIG['application_interface']);
            else:
                raise NotImplementedError('No implementation for application_interface = ' + THYWILL_CONFIG['application_interface']['component'])   
        return ApplicationInterfaceComponent.singleton 

    def __init__(self, config):
        '''
        Constructor.    
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        raise NotImplementedError()

    def send_message_to_client(self, uuid, raw_message):
        '''
        Called by the application: send a message to a specific client.
        
        :Parameters:
            - uuid: unique identifier for a specific client
            - raw_message: The message to be sent
        '''
        raise NotImplementedError()

    def client_message_received(self, uuid, raw_message):
        '''
        Called by thywill to notify the application of a client message received by the receive component
        
        :Parameters:
            - uuid: unique identifier for a specific client
            - raw_message: The message to be sent
        '''
        raise NotImplementedError()   
        
    