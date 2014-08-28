Demo Notes
##########

This demo is based on `Socket.io <http://socket.io/get-started/chat/>`_ but we are
going to write the backend system in Python. Hence, we also go with a chat app.

Generally, people go with **Socket.io** which is quicker since anyone can use
the demo code as a starting point and it is pretty well implemented. Unfortunately,
Tornado Framework does not have one.

.. note:: This demo uses : 3 as a wrapper to Tornado.

Since this session is only half an hour, we will use the code from https://github.com/shiroyuki/voila-hmmx.

Preparation
===========

The user interface
==================

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
