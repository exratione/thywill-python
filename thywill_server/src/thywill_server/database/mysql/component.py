
from thywill_server.database.database_component import DatabaseComponent

class MysqlComponent(DatabaseComponent):
    '''
    Configuration and helpers for MySQL as the database.
    '''
    
    

    def __init__(self, config):
        '''
        Constructor
        '''
        self.database = config['database']
        self.user = config['user']
        self.password = config['password']
        self.host = config['host']
        self.port = config['port']


    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''   
        pass