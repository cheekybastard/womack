Womack config
=============

Womack's configuration is stored in a Config object in the
``womack.config`` module. 

When running the server, this config object
is initialized by command-line arguments.

When using a :class:`womack.publish.Publisher`, the configuration is
loaded when the instance is instantiated. So to change defaults, you
must set config settings *before instantiating the Publisher*::

  >>> from womack import config, publish
  >>> config.config.redis_host = 'example.com'
  >>> config.config.key = 'something-else'
  >>> wm = publish.Publisher()
  >>> wm.key
  'something-else'

(Of course you can also pass non-default arguments to the Publisher to
configure it that way).
