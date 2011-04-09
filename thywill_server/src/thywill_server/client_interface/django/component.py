
from thywill_server.application_interface.application_interface_component import ApplicationInterfaceComponent
from thywill_server.client_interface.client_interface_component import ClientInterfaceComponent
from thywill_server.client_interface.django.django_client_configuration import DjangoClientConfiguration
from thywill_server.log.log_component import LogComponent
from thywill_server.push.push_component import PushComponent
from thywill_server.database.database_component import DatabaseComponent

class DjangoComponent(ClientInterfaceComponent):
    '''
    Configuration and helpers for Django as the web server.
    '''

    def __init__(self, config):
        '''
        Constructor.
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        self.static_path = config['static_path']
        self.template_path = config['template_path']
        self.port = config['port']
        self.secure = config['secure']
        self.hostname = config['hostname']
        self.secret_key = config['secret_key']

    def create_client_configuration(self, uuid):
        '''
        Return information to pass to the client so it can configure its expectations accordingly.
        This is built from the input of various components in the thywill system, and the provided
        additional_parameters.
        
        :Parameters:
            - uuid: a string ID for this client
            
        :Return:
            ClientConfiguration object
        '''
        
        # create a client configuration object. The additional parameters
        # dictionary is used to add in the uuid for a specific client.
        config = DjangoClientConfiguration(uuid)

        # add data from this component
        self._bootstrap_client(uuid, config)
        
        # add data from the other components; ordering should be such that
        # the application interface component is last, as that gives it a chance
        # to see what else is set.
        LogComponent.factory()._bootstrap_client(uuid, config)
        PushComponent.factory()._bootstrap_client(uuid, config)
        DatabaseComponent.factory()._bootstrap_client(uuid, config)
        ApplicationInterfaceComponent.factory()._bootstrap_client(uuid, config)
        
        return config;

    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''   
        client_configuration._set_bootstrap_parameter('send_path', '/thywill/send/')
        client_configuration._set_bootstrap_parameter('send_data_type', 'json')
        client_configuration._set_bootstrap_parameter('static_path', self.static_path)
        client_configuration._add_bootstrap_resource({
            'type': 'javascript',
            'resource': self.static_path + '/client_interface/django/jquery.js'
        })
        client_configuration._add_bootstrap_resource({
            'type': 'javascript',
            'resource': self.static_path + '/client_interface/django/thywill.js'
        })



