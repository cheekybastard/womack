Womack server
=============

.. note ::

   Womacks's pip requirements files are split into a base file
   (``requirements.txt``) and a server file
   (``requirements-server.txt``). To run the server, you must install
   ``requirements-server.txt``, which includes the extra requirements
   needed by the server. The ``make server`` command will do this, or
   ``pip install -r requirements-server.txt``.

Running the server
------------------

In the simplest case -- you want to use Womack to push events to
clients, and don't need to customize anything -- you can just run the
``womack`` script. It accepts a number of command-line arguments.

.. program:: womack

.. option:: -H, --host

   The hostname or ip to serve on. Default: 0.0.0.0

.. option:: -p, --port

   The port to bind to. Default: 8111

.. option:: --redis-host

   The host where redis is running. Default: localhost

.. option:: --redis-port

   The port where redis is running. Default: 6379

.. option:: --debug

   Output debugging information to the console. Default: False


Customizing the server
----------------------

See :doc:`namespace` for information about customizing Womack's
handling of socketio namespaces. You can use a namespace to customize how
messages are passed in your Womack-using system.

If besides (or instead of) that you want to customize how the server
is run (for instance, to turn on the flash policy server, which is off
by default, or to daemonize the server), you have to deal with a few
phases of execution:

Configuration
~~~~~~~~~~~~~

You can use :func:`womack.server.parse_argv` to parse command line
options -- if you want to use the same ones -- or parse them yourself
and call :meth:`womack.config.config.configure` to configure the
Womack server.

.. autofunction :: womack.server.parse_argv

Running
~~~~~~~

Womack is based on `bottle`_ and uses the standard
:class:`socketio.SocketIOServer` to serve the bottle application that
is configured in ``womack.server``:

.. literalinclude :: ../womack/server.py
   :language: python
   :lines: 48-54

You can do the same thing, just pass ``womack.server.app`` to a
SocketIOServer in the configuration of your choice, and run it.

.. _bottle: http://bottlepy.org
