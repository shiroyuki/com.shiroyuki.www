Demo Notes
##########

This demo is based on `Socket.io <http://socket.io/get-started/chat/>`_ but we
are going to write the backend system in Python.

High-level Architecture Overview
================================

.. blockdiag::

    blockdiag {
        HTTP_Module -> WS_Module;
        WS_Module -> RabbitMQ;
        WS_Module -> MongoDB;
    }

where:

- **HTTP_Module** is to serve the user interfaces,
- **WS_Module** is to provide and manage web socket connections, messages and auditing,
- **RabbitMQ** is for message exchange,
- **MongoDB** is for auditing.

.. warning:: Writing in progress.
