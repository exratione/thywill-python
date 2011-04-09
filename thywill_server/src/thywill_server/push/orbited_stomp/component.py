
from thywill_server.push.push_component import PushComponent
from thywill_server.push.orbited_stomp.stomp_message import StompMessage
from thywill_server.log.log_component import LogComponent
import stomp

class OrbitedStompComponent(PushComponent):
    '''
    Configuration and helpers for the Orbited server and STOMP protocol as an implementation of AJAX push.
    This will likely be an Orbited instance and a separate STOMP-speaking message queue server like CoilMQ.
    '''
    
    def __init__(self, config):
        '''
        Constructor.
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        self.orbited_static_path = config['orbited_static_path']
        self.orbited_port = config['orbited_port']
        self.orbited_secure = config['orbited_secure']
        self.orbited_hostname = config['orbited_hostname']  
        
        # Orbited is a relay: it connects to the STOMP server, not the client.
        # So these values are from the perspective of the Orbited server, not the client.
        # If you are running Orbited and the STOMP server on the same machine, stomp_hostname will be localhost     
        self.stomp_port = config['stomp_port']
        self.stomp_hostname = config['stomp_hostname']
  
  
    def push_to_client(self, uuid, message):
        '''
        Push a message to a particular client via a STOMP server
        
        :Parameters:
            - uuid: The unique client identifier ID
            - message: A StompMessage object
        '''
        
        # TODO add a listener to connection to get confirmation of delivery?
        # TODO connection pool strategy
        # stomp.py docs: http://code.google.com/p/stomppy
        LogComponent.debug(['OrbitedStompComponent.push_to_client', self.stomp_hostname, self.stomp_port, uuid, message])
        conn = stomp.Connection([(self.stomp_hostname, self.stomp_port)])
        conn.start()
        conn.connect()
        conn.send(message=message.contents, destination=uuid, type='textMessage', ack='auto')
        conn.disconnect() # or conn.stop() - different behavior if there are listeners

    def wrap_push_message(self, raw_message):
        '''
        Wrap a raw message in the object needed for push_to_client.
        
        :Parameters:
            - raw_message: The message to be sent
            
        :Return:
            StompMessage object.
        '''
        return StompMessage(raw_message)

    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''     
        client_configuration._add_bootstrap_resource({
            'type': 'javascript',
            'resource': self.__get_url(self.orbited_secure, self.orbited_hostname, self.orbited_port, '/static/Orbited.js'),
        })
        client_configuration._add_bootstrap_resource({
            'type': 'javascript',
            'resource': self.__get_url(self.orbited_secure, self.orbited_hostname, self.orbited_port, '/static/protocols/stomp/stomp.js'),
        })
        client_configuration._add_bootstrap_resource({
            'type': 'javascript',
            'resource': self.__get_url(self.orbited_secure, self.orbited_hostname, self.orbited_port, self.orbited_static_path + '/bootstrap.js'),
        })
        client_configuration._set_bootstrap_parameter('stomp_hostname', self.stomp_hostname)
        client_configuration._set_bootstrap_parameter('stomp_port', self.stomp_port)
        client_configuration._set_bootstrap_parameter('channel', uuid)
  
        
    def __get_url(self, secure, host, port, path):
        if secure:
            url = 'https://'
        else:
            url = 'http://'
        return url + host + ':' + str(port) + path;   

        
    