
from thywill_server.component import Component
from thywill_server.settings import THYWILL_CONFIG

class LogComponent(Component):
    '''
    The parent class for log component definitions.
    '''
    singleton = None
    
    DEBUG = 'debug'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    CRITICAL = 'critical'
    
    @staticmethod
    def factory():
        '''
        Get the log component object.
        '''
        if not LogComponent.singleton:
            if THYWILL_CONFIG['log']['component'] == 'file':
                from thywill_server.log.logfile.component import LogfileComponent
                LogComponent.singleton = LogfileComponent(THYWILL_CONFIG['log']);
            else:
                raise NotImplementedError('No implementation for log = ' + THYWILL_CONFIG['log']['component'])   
        return LogComponent.singleton 

    def __init__(self, config):
        '''
        Constructor.    
        '''
        raise NotImplementedError()
    
    @staticmethod
    def log(level, message):
        '''
        Log a message.
        
        :Parameters:
            - level: the log level, e.g. LogComponent.DEBUG
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.factory().log(level, message)
    
    @staticmethod
    def debug(message):
        '''
        Log at the debug level.
        
        :Parameters:
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.log(LogComponent.DEBUG, message)
        
    @staticmethod
    def info(message):
        '''
        Log at the info level.
        
        :Parameters:
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.log(LogComponent.INFO, message)
        
    @staticmethod
    def warning(message):
        '''
        Log at the warning level.
        
        :Parameters:
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.log(LogComponent.WARNING, message)
        
    @staticmethod
    def error(message):
        '''
        Log at the error level.
        
        :Parameters:
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.log(LogComponent.ERROR, message)
        
    @staticmethod
    def critical(message):
        '''
        Log at the critical level.
        
        :Parameters:
            - message: message to be logged: can be anything that responds to str(message)
        '''
        LogComponent.log(LogComponent.CRITICAL, message)
        