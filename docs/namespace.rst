Womack namespace
================

Womack provides a namespace registry that you can use to easily inject
different message handlers into the socketio server. This is how you
might extend Womack to manage chat room rosters, for example.

By default, one instance of :class:`womack.namespace.Namespace` is
injected, using the default socketio namespace.

If your application requires separation of connections into multiple
namespaces but no additional logic, you can register multiple copies
of the default namespace handler::

   >>> from womack import namespace, server
   >>> namespace.register('/another', namespace.Namespace)
   >>> namespace.register('/still-more', namespace.Namespace)
   >>> server.main()

Or, you can subclass :class:`womack.namespace.Namespace` (or its base
class, :class:`socketio.namespace.BaseNamespace`) and register
your subclass as the default handler (''), or at another namespace.

After registering namespaces you have to start the server somehow,
for instance by calling ``server.main``. See :doc:`server` for
more information about that.

.. automodule :: womack.namespace
   :members:
   :show-inheritance:
