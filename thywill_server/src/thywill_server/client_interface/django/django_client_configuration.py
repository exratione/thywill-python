
from thywill_server.client_interface.client_configuration import ClientConfiguration
import simplejson as json

class DjangoClientConfiguration(ClientConfiguration):
    
    def __init__(self, uuid, bootstrap_parameters = {}):
        '''
        Constructor.
        
        :Parameters:
            bootstrap_parameters: a dictionary
        '''
        ClientConfiguration.__init__(self, uuid, bootstrap_parameters)
        
        
    def to_json(self, formatted = False):
        '''
        Return a JSON representation of the client configuration data.
        
        :Parameters:
            - formatted - True|False, return a formatted, indented string if true.
            
        :Return:
            A JSON string representation.
        '''
        if formatted: 
            return json.dumps(self.to_dict(), indent = '\t')
        else:
            return json.dumps(self.to_dict())