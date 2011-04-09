

class ClientConfiguration(object):
    '''
    A container class for configuration information used by the client. 
    '''


    def __init__(self, uuid, bootstrap_parameters = {}):
        '''
        Constructor.
        
        :Parameters:
            bootstrap_parameters: a dictionary
        '''
        self.uuid = uuid
        self.bootstrap_parameters = {}
        self.bootstrap_resources = []
        self.application_parameters = {}
        self.application_resources = []
        
        for name in bootstrap_parameters:
            self._set_bootstrap_parameter(name, bootstrap_parameters[name])  
    
    def _add_bootstrap_resource(self, resource):
        '''
        Add a resource for the client to use as a part of the thywill bootstrap process.
        
        :Parameters:
            - resource: { 'type': string, 'resource': string }
        '''
        self.bootstrap_resources.append(resource)
        
    def _set_bootstrap_parameter(self, name, value):
        '''
        Set a parameter to be passed to the client to use as a part of the thywill bootstrap process. 
        Existing values are overwritten.
        
        :Parameters:
            - name: new parameter name
            - value: new parameter value
        '''
        self.bootstrap_parameters[name] = value

    def add_application_resource(self, resource):
        '''
        Add a resource for the application that will run on the client.
        
        :Parameters:
            - resource: { 'type': string, 'resource': string }
        '''
        self.application_resources.append(resource)
        
    def set_application_parameter(self, name, value):
        '''
        Set an application parameter to be passed to the client. Existing values are overwritten.
        
        :Parameters:
            - name: new parameter name
            - value: new parameter value
        '''
        self.application_parameters[name] = value
                
    def to_dict(self):
        '''
        :Return:
            A dictionary representation of the configuration data.
        '''
        return {
            'uuid': self.uuid,
            'bootstrap_resources': self.bootstrap_resources,
            'bootstrap_parameters': self.bootstrap_parameters,
            'application_resources': self.application_resources,    
            'application_parameters': self.application_parameters,   
        }