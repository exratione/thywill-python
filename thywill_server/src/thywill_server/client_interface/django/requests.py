'''
Functions used to build pages.
'''

from thywill_server.client_interface.client_interface_component import ClientInterfaceComponent
from thywill_server.application_interface.application_interface_component import ApplicationInterfaceComponent
from thywill_server.log.log_component import LogComponent
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
import uuid

def thywill(request):
    '''
    Deliver the basic thywill framing page, immediately prior to bootstrap.
    
    :Parameters:
        - request: HttpRequest
        
    :Return:
        HttpResponse
    '''
    uuid = __ensure_uuid(request)
    config = ClientInterfaceComponent.factory().create_client_configuration(uuid)
    context = Context({
        'config': config.to_dict(),
        'config_json': config.to_json(True),
    })
    LogComponent.debug(['django.requests.thywill', 'initial client page load', uuid, config.to_dict()])
    return HttpResponse(get_template('thywill.html').render(context))
 
def send(request):
    '''
    AJAX response: Send a client-originated message into the currently active application.
    
    :Parameters:
        - request: HttpRequest
            
    :Return:
        HttpResponse
    '''
    uuid = __ensure_uuid(request)
    if 'message' in request.POST:
        message = request.POST['message']
        LogComponent.debug(['django.requests.send', 'AJAX message from client', uuid, message])
        ApplicationInterfaceComponent.factory().client_message_received(uuid, message)
    else:
        LogComponent.debug(['django.requests.send', 'Invalid POST request', uuid, request.POST])
    
    # TODO return confirmation of some sort?
    
    
    return HttpResponse()


def __ensure_uuid(request):
    '''
    Set a unique user ID (uuid) for the session if one doesn't exist, or return the existing uuid.
    
    :Return:
        uuid string
    '''
    if not request.session.get('uuid', None):
        request.session['uuid'] = str(uuid.uuid4())
    return request.session['uuid'];  
    