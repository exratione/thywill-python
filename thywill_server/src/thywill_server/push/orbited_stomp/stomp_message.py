
from thywill_server.push.push_message import PushMessage

class StompMessage(PushMessage):
    '''
    Representing a STOMP protocol message intended to be pushed out to a client.
    '''

    def __init__(self, contents):
        '''
        Constructor.
        '''
        self.contents = contents
        
        
        