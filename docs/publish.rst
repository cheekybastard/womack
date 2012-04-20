Womack publisher
================

To publish events to clients, use a :class:`womack.publish.Publisher`
instance that is configured to connect to the same redis server as the
socket server serving the clients. Then when you publish on a channel,
clients who have subscribed to that channel will receive the message.

Reference
---------

.. automodule :: womack.publish
   :members:
