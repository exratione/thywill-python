
from thywill_server.component import Component
from thywill_server.settings import THYWILL_CONFIG

class DatabaseComponent(Component):
    '''
    The parent class for web server component definitions.
    '''
    singleton = None
    
    @staticmethod
    def factory():
        '''Get the database component object.'''
        if not DatabaseComponent.singleton:
            if THYWILL_CONFIG['database']['component'] == 'mysql':
                from thywill_server.database.mysql.component import MysqlComponent
                DatabaseComponent.singleton = MysqlComponent(THYWILL_CONFIG['database']);
            else:
                raise NotImplementedError('No implementation for database = ' + THYWILL_CONFIG['database']['component'])   
        return DatabaseComponent.singleton 

    def __init__(self, config):
        '''
        Constructor.    
        '''
        raise NotImplementedError()