thywill-python development setup on Windows
-------------------------------------------

Follow these instructions to set up a development environment on Windows for working with thywill-python.

1) install GitTortoise

  * Which means installing msysgit
  * See: http://code.google.com/p/tortoisegit/

2) install Python

  * Default location is C:\Python27
  * Add C:\Python27 and C:\Python27\Scripts to the path

3) Install setuptools:

  * Download: http://peak.telecommunity.com/dist/ez_setup.py
  * Put it in C:\Python\Tools\setuptools
  * cd C:\Python27\Tools\setuptools
  * python ez_setup.py setuptools

4) To use the setuptools to install Orbited and its dependencies, you'll need a compiler from a MinGW install. See: http://orbited.org/wiki/InstallationWindows

  * Run on command prompt: easy_install orbited
  * But this will fail on Twisted. See: http://blog.eddsn.com/2010/05/unable-to-find-vcvarsall-bat/
  * This is a fairly long install of a GNU environment.
  * If you installed MinGW for example to "C:\MinGW" then add "C:\MinGW\bin" to your path
  * Have to download Twisted directly - the URL will be in the failed attempt
  * Put it into C:\Python27\Lib\site-packages and unzip it, then cd into the Twisted-* folder
  * Once there: python setup.py install build --compiler=mingw32
  * Then go back and install orbited again via easy_install, and it will work
  * Then you have to have copy some files around: see URL above. Only necessary if you want to run orbited versus just using the libraries in development.

5) Install the simplejson Python package

  * Docs at: http://simplejson.github.com/simplejson/
  * Run at the command prompt: easy_install simplejson

6) Install the stomp.py Python package

  * Docs at: http://code.google.com/p/stomppy/
  * (But note that the wiki examples are very out of date).
  * Run at the command prompt: easy_install stomp.py

7) install Django

  * this will create the Django libraries with the Python install

8) install Eclipse Classic 3.6.2 or later

  * install PyDev:
  * see: http://www.vogella.de/articles/Python/article.html
  * if you avoid a number of odd problems, make sure you completely install Python and Django before installing PyDev. If you install Django afterwards, it won't recognize that it exists, and you'll have to remove the interpreter setting and recreate it.
  * install the Web Page Editor component:
  * Help" > "Install New Software" Choose to work with the site for your version of eclipse.
  * Expand "Web, XML and Java EE development", check "Web Page Editor" and click Next to continue with the install

9) install MySQL

  * create a database "thywill" and a user "thywill" with password "dummy_password" with permissions to access from localhost

10) clone the repository for thywill to your local machine.

11) import the projects from the Git repository into Eclipse.

  * /thywill_apps
  * /thywill_server

