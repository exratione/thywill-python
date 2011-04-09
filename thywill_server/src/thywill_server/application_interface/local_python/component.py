
from thywill_server.application_interface.application_interface_component import ApplicationInterfaceComponent
from thywill_server.push.push_component import PushComponent
from thywill_server.log.log_component import LogComponent

class LocalPythonComponent(ApplicationInterfaceComponent):
    '''
    Configuration and helpers for a thywill application that runs in this Python thread.
    '''
    
    def __init__(self, config):
        '''
        Constructor.
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        self.application_package = config['application_package'];
        package = __import__(self.application_package, fromlist = ['thywill_interface']);
        self.app_interface_module = getattr(package, 'thywill_interface')
        
    def send_message_to_client(self, uuid, raw_message):
        '''
        Send a message to a specific client.
        '''
        LogComponent.debug(['LocalPythonComponent.send_message_to_client', uuid, raw_message])
        PushComponent.factory().push_raw_message_to_client(uuid, raw_message)

    def client_message_received(self, uuid, raw_message):
        '''
        Notify the application of a client message received by the receive component
        '''
        LogComponent.debug(['LocalPythonComponent.client_message_received', uuid, raw_message])
        self.app_interface_module.message_from_client(uuid, raw_message);

    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''    
        client_configuration._set_bootstrap_parameter('application_package', self.application_package)
        self.app_interface_module._bootstrap_client(uuid, client_configuration)
        
        