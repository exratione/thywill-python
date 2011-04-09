from django.conf.urls.defaults import patterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    
    # Initial page load, with bootstrap configuration of thywill
    (r'^thywill/init/', 'thywill_server.client_interface.django.requests.thywill'),    
    
    # General client ajax, used to send messages
    (r'^thywill/send/', 'thywill_server.client_interface.django.requests.send'),
    
)

handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'
