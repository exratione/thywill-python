
from thywill_server.component import Component
from thywill_server.settings import THYWILL_CONFIG

class PushComponent(Component):
    '''
    The parent class for push component definitions.
    '''
    singleton = None

    @staticmethod
    def factory():
        '''Get the push component object.'''
        if not PushComponent.singleton:
            if THYWILL_CONFIG['push']['component'] == 'orbited stomp':
                from thywill_server.push.orbited_stomp.component import OrbitedStompComponent
                PushComponent.singleton = OrbitedStompComponent(THYWILL_CONFIG['push']);
            else:
                raise NotImplementedError('No implementation for receive = ' + THYWILL_CONFIG['push']['component'])  
        return PushComponent.singleton
        
    def __init__(self, config):
        '''
        Constructor.    
        
        :Parameters:
            - config: a dictionary of configuration information
        '''
        raise NotImplementedError()
    
    def push_raw_message_to_client(self, uuid, raw_message):
        '''
        A convenience method equivalent to push_to_client(uuid, self.wrap_push_message(raw_message))
        
        :Parameters:
            - uuid: The unique client identifier ID
            - raw_message: The message to be sent
        '''
        self.push_to_client(uuid, self.wrap_push_message(raw_message))
    
    def push_to_client(self, uuid, message):
        '''
        Push a message to a particular client.
        
        :Parameters:
            - uuid: The unique client identifier ID
            - message: A PushMessage object
        '''
        raise NotImplementedError()
    
    def wrap_push_message(self, raw_message):
        '''
        Wrap a raw message in the object needed for push_to_client.
        
        :Parameters:
            - raw_message: The message to be sent
            
        :Return:
            PushMessage object.
        '''
        raise NotImplementedError()
    

