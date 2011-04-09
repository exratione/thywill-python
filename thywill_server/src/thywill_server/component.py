
class Component(object):
    '''
    The parent class for the various thywill component definitions. Not intended to be instantiated.
    '''
    
    def __init__(self, config):
        '''
        Constructor.    
        
        :Parameters:
            - config: a dictionary of configuration information
        '''
        raise NotImplementedError

    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''   
        raise NotImplementedError()
    
