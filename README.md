thywill-python
--------------

thywill-python is a simple Python and Javascript framework that glues together a Comet server, a web server, and many client web browsers. Asynchronous messaging applications built on top of thywill-python are written in Python (server-side) and Javascript (client-side). The thywill-python framework manages client browser connections and message delivery, so that the application author can focus on everything else.

thywill-python is the result of a newcomer's short exploration of (a) Python and (b) Comet techniques for pushing data to browsers over HTTP connections. e.g. for applications such as multi-player games and chat servers built in modern web browsers using Javascript, AJAX, canvas, and the like. All the cool kids are using node.js for that these days, but it took long enough to learn that fact to be able to build thywill-python along the way.

This is functional, documented, but prototype code. The thywill-python packages may be a useful starting point for someone intending to build a messaging-based Comet server application, and who is determined to use Python for the job.

Framework and Component Abstractions
------------------------------------

thywill-python consists of glue code and a bootstrap framework to hold together some unknown future combination of server and client technology choices. It is structured as a set of component abstractions: on connection by a client browser, implementations of these component abstractions are managed in a bootstrap process wherein each component independently contributes configuration and Javascript code to run in the client.

The component abstractions and their present implementations are as follows:

<h3>Application Interface</h3>

What it does: Manages communication with the application built on top of thywill-python. The application decides what to do with client messages and what to send back to connected clients.

Implementation: The application is a local Python package.

<h3>Client Interface</h3>

What it does: manages the interface to the client. It accepts messages from the client, assigns client sessions and unique IDs, and so forth.

Implementation: a Django web server.

<h3>Database</h3>

What it does: manages the database layer.

Implementation: MySQL

<h3>Log</h3>

What it does: Manages logging for the framework and application.

Implementation: standard Python logging.

<h3>Push</h3>

What it does: Manages sending asynchronous messages to specific clients, e.g. through a Comet server.

Implementation: Orbited, using the STOMP protocol and the MorbidQ stomp broker packaged with Orbited.

Configuring thywill-python
--------------------------

To configure thywill-python, edit /thywill-server/src/thywill_server/settings.py

This file contains the definitions for the component implementations to use, and the parameters passed to those implementations.

Bootstrap Process and Test Application
--------------------------------------

The bootstrap process connects a client to the various server components, and makes the system ready for an application built on top of thywill-python to run. See the image files in /documentation for a clear explanation of what the components of thywill-python are, and how the bootstrap process works in practice. 

After the bootstrap process completes, thywill is ready to load and run an application written in Python (server side) and Javascript (client side).

A single trivial application and application interface example is provided in /thywill_apps. It is a proof of concept application to test that the system is working, and that messages from a specific client - and addressed to that same client - can make the round trip through thywill-python and return.

Thywill Bootstrap for a Browser Client
--------------------------------------

This is an outline of the bootstrap process for a browser client. See the image files in /documentation for diagrams of this process.

1) An HTML page is loaded from /thywill/init/, containing calls to Javascript files that are added in by the various component implementations and the designated application. 

2) These Javascript files are divided into bootstrap Javascript and application Javascript.

3) The bootstrap Javascript code is loaded first and carries out the process of connecting to the Comet server and setting up data structures as needed.

4) The application Javascript code is loaded secondmost - but while the bootstrap process is still continuing. 

5) The application Javascript code carries out the following activities:
  * Sets up its own environment for display and data entry
  * Sets callback functions in the main thywill data structure
  * Passes a startup function to thywill that is called when the bootstrap process is complete.

6) Thus the application sets itself up in parallel to the bootstrap process, and then waits for confirmation before continuing. 

7) The application manages whatever errors are displayed to the user as a result of issues with the bootstrap.

Why Use thywill-python?
-----------------------

  * Because it makes it one step easier to build a Comet-based asynchronous messaging application from scratch in Python.

  * Because you really like working with Python code written by someone who was learning Python at the time.

But seriously: If you like node.js, then you should use node.js instead - it is a much simpler and more reliable way to produce the same end result achieved in thywill-python. It requires fewer different pieces of supporting software. If you're going to be writing complex client-side Javascript, why not use a system wherein you can write the server side in Javascript as well? That is an important consideration when it comes to whether you are going to find adoption amongst developers.

The following caveats apply to using thywill as it is:

  * The MorbidQ server that comes with Orbited is not intended for use at scale. You will need to set up a different configuration and use a stand-alone STOMP broker.

  * Orbited works well but is not as well supported as other similar Comet projects. Consider replacing it with APE ( http://www.ape-project.org/ ) or node.js (and of course writing the component implementations to manage those server instances in the framework).

  * The Django client interface component is set up in a development configuration, completely unsuitable for production use.

  * thywill-python is not tested at scale, or indeed in any way tested comprehensively. It works for the author, and that's all the guarantee you'll get.


