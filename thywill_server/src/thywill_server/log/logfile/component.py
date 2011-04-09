
from thywill_server.log.log_component import LogComponent
import logging
import logging.handlers

class LogfileComponent(LogComponent):
    '''
    Configuration and helpers for logging to file through the standard Python logging and logging.handlers packages. 
    
    Note that if you are running this log component, other third party packages using logging may also write
    to the log file used by this package. This may or may not be a bonus from your point of view, but be aware that it will happen.
    '''

    LEVEL_MAP = {
        LogComponent.DEBUG: logging.DEBUG,
        LogComponent.INFO: logging.INFO,
        LogComponent.WARNING: logging.WARNING,
        LogComponent.ERROR: logging.ERROR,
        LogComponent.CRITICAL: logging.CRITICAL,
    }

    def __init__(self, config):
        '''
        Constructor.
        
        :Parameters:
            - config: dictionary of configuration parameters.
        '''
        self.path = config['path']
        self.level = config['level']

        level = LogfileComponent.LEVEL_MAP.get(self.level, logging.NOTSET)
        logging.basicConfig(level=level)
        self.logger = logging.getLogger()
        handler = logging.handlers.RotatingFileHandler(self.path + '/thywill.log', maxBytes=2000000, backupCount=5)
        self.logger.addHandler(handler)

    def log(self, level, message):
        '''
        Log a message.
        
        :Parameters:
            - level: the log level, e.g. LogComponent.DEBUG
            - message: message to be logged: can be anything that responds to str(message)
        '''
        log_level = LogfileComponent.LEVEL_MAP.get(level, logging.NOTSET)
        self.logger.log(log_level, str(message))

    def _bootstrap_client(self, uuid, client_configuration):
        '''
        Take the necessary actions for a new client, such as adding to the client_configuration.
        
        :Parameters:
            - uuid: a string ID for this client
            - client_configuration: a ClientConfiguration object.
        '''   
        pass