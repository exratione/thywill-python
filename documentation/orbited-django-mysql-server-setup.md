thywill-python server: Orbited + Django + Apache + MySQL
--------------------------------------------------------

This document outlines one possible configuration for a secure thywill server, using largely Python-based software, and STOMP as the protocol for messaging, with all client traffic passing over encrypted connections.

- Orbited is the Comet server, acting as a proxy to connect the browser client to the message queue.
- Orbited's attached message queue package, MorbidQ is used.
- Django connected to Apache via WSGI provides the web server.
- MySQL is the database.

The component implementations used internally to thywill-python to support this configuration are:

  * database: mysql
  * client_interface: django
  * push: orbited_stomp

Server
------

We will use an Amazon AWS server for the purposes of this document.

Starting point: Fedora Core 14
AWS AMI: ami-225aac4b

Installation of necessary packages
----------------------------------

    yum install python stomppy httpd mod_ssl Django monit mysql mysql-server MySQL-python mod_wsgi 
    chkconfig --level 2345 monit on
    chkconfig --level 2345 httpd on
    chkconfig --level 2345 orbited on
    chkconfig --level 2345 mysqld on

MySQL
-----

Create a user and database:

    create database thywill;
    grant all on thywill.* to 'thywill'@'localhost' identified by 'dummy_password';

Configure my.cnf as you see fit.

Orbited
-------

Orbited is set up to maintain Comet-style connections to browsers. See: http://orbited.org/wiki/Installation

  * Listen on port 8443
  * Start up the MorbidQ message broker using the STOMP protocol on port 61613
  * Serve static files from part of the thywill project.

Create a snakeoil certificate (or get a real one): the following commands are for the snakeoil. They creates a key with a pass, removes the pass, and creates a certificate.

    mkdir /etc/orbited
    cd /etc/orbited
    openssl genrsa -des3 -out orbited.key-with-pass 2048
    openssl req -new -key orbited.key-with-pass -out orbited.csr
    openssl rsa -in orbited.key-with-pass -out orbited.key
    openssl x509 -req -days 365 -in orbited.csr -signkey orbited.key -out orbited.crt

Note that you may find that requests to Orbited on port 8443 won't work with snakeoil certificates - and will fail fairly silently - until you visit an Orbited url directly and click through whatever your browser warning is for invalid SSL certificates.

Configuration directives are as follows. Mix them into your /etc/orbited.cfg as you see fit:

    [global]
    reactor=epoll
    user=orbited
    session.ping_interval=100
    session.ping_timeout=100
    proxy.enabled=1

    [listen]
    https://:8443
    stomp://61613

    [ssl]
    key=/etc/orbited/orbited.key
    crt=/etc/orbited/orbited.crt

    [access]
    * -> localhost:61613

    [static]
    s=/var/www/thywill-python/thywill_server/static/push/orbited_stomp

    [logging]
    debug=/var/log/orbited/debug.log
    info=/var/log/orbited/info.log
    access=/var/log/orbited/access.log
    warn=/var/log/orbited/warn.log
    error=/var/log/orbited/error.log

    enabled=info,access,warn,error

For version 0.7.1 as installed via package on FC14, you have to make a minor edit to /etc/init.d/orbited in order to allow binding to privileged ports such as port 443. Comment out the top line, replace with the bottom one.

    #daemon --user $prog --check $prog $prog --daemon
    daemon --check $prog $prog --daemon

Django
------

Apache is the web server, and sends requests to be served by Django via mod_wsgi. See:

http://code.google.com/p/modwsgi/
http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango
http://docs.djangoproject.com/en/dev/howto/deployment/modwsgi/

Set up the Apache configuration as follows to listen on ports 80 and 443.

Listen on port 80, but redirect all traffic to 443. e.g.:

    RewriteEngine On
    RewriteRule ^(.*)$ https://mydomain.com$1 [QSA,L]

Listen on port 443 and send requests to static files and Django as appropriate. e.g:

    Alias /robots.txt /var/www/thywill-python/thywill_server/static/robots.txt
    Alias /favicon.ico /var/www/thywill-python/thywill_server/static/favicon.ico
    Alias /static/ /var/www/thywill-python/thywill_server/static/
    Alias /apps/ /var/www/thywill-python/thywill_apps/static/

    <Directory /var/www/thywill-python/thywill_apps/static/>
        Order deny,allow
        Allow from all
    </Directory>

    <Directory /var/www/thywill-python/thywill_server/static/>
        Order deny,allow
        Allow from all
    </Directory>

    WSGIScriptAlias / /var/www/thywill-python/thywill_server/django_static/wsgi/django.wsgi

Firewall
--------

Here, use the AWS firewall rather than a server firewall like IPtables. Set the following configuration:

  * Open to the world: 80, 443, 8443
  * Restricted: 22
  * All outgoing allowed, all others closed to incoming traffic

thywill-python code
-------------------

Clone the git repository into /var/www/thywill-python

If you change this location, you will have to adjust the various paths that assume it:

  * in your Apache and Orbited configuration
  * in the thywill_server/django_static/wsgi/django.wsgi file

To initialize various items (e.g. the Django database setup), run the rollowing commands:

    cd /var/www/thywill-python/thywill_server/src
    python initialize.py

Create a log directory, and give it suitable permissions:

    mkdir /var/log/thywill
    chown apache:apache /var/log/thywill

thywill-python configuration
----------------------------

The thywill configuration is presently hardcoded in var/www/thywill/thywill_server/src/settings.py. It is a simple set of component declarations and the parameters for component configuration.

In settings.py, you must set the values of:

    THYWILL_ROOT = /var/www/thywill-python
    THYWILL_HOST = mydomain.com

Odds and Ends
-------------

You may need to install the simplejson Python package. Documentation at: http://simplejson.github.com/simplejson/

    easy_install simplejson

Kick the Tires
--------------------------------------

At this point the rudimentary thywill proof of concept application should work. It demonstrates nothing more than a round trip of messages through thywill from client and back again.

Point a browser to https://mydomain.com/thywill/init/. Messages sent via AJAX should be returned via Orbited and displayed.
