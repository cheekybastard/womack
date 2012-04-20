Womack client
=============

To receive Womack events in the client, pull Womack's script into the
page, and instantiate a Womack:

.. code-block :: html

   <html>
     <head>
       <script src="http://localhost:8111/womack.js"></script>
     </head>
     <body>
       <!-- ... your page here -->

       <script>
         var womack = new Womack();
         womack.on('connect', function () { /* ... */ });
         womack.on('disconnect', function () { /* ... */ });
         womack.subscribe('the channel', function (message) { /* ... */ });
       </script>
    </body>
  </html>

If you need direct access to `socket.io`_ functions, you can access
them via the womack instance's ``io`` property.

Reference
---------

.. js:class:: Womack([options])

   Womack client, used to receive messages from a Womack server.

   :param options: Additional options for Womack or socket.io.
                   The most important ones are ``host`` and ``port``.

                   ``host`` is the host to connect to. It defaults
                   to the *host that the script was served from*
                   -- if that can be found -- or
                   ``window.location.hostname``.

                   ``port`` is the port to connect to. That
                   defaults to the *port that the script was served
                   from* -- if that can be found -- or
                   ``window.location.portname``.

   .. js:function:: on(event, callback)

      Register a callback for a socket event. Most common events
      to watch for are ``"connect"`` and ``"disconnect"`` -- but
      you can register a callback for any socket.io event.

   .. js:function:: subscribe(channel, callback)

      Subscribe to a Womack channel. This is the primary client
      interface (at least for the stock Womack server). This
      will register your socket as a receiver of messages on the
      given channel, and your callback will be called with the
      message (already decoded from JSON) whenever a message
      is published to that channel by a
      :class:`womack.publish.Publisher` that is connected to
      the same redis server that the socket server is
      connected to.

   .. js:attribute:: io

      The socket.io object that Womack uses to communicate
      with the socket server.


.. _socket.io: http://socket.io/
