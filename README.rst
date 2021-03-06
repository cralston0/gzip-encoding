=============
gzip-encoding
=============

Examples of how to upload gzip-compressed HTTP **requests** to a web server
and process these requests on the server.

Background
==========

There's a lot of misleading snippets on the Internet about this topic, as
we learned when we tried to implement the ability to gzip data uploaded
from our clients to the cloud.

While there are clear standards on how to gzip data in an HTTP response
(such as when compressing HTML and CSS to send to a web browser) there
doesn't appear to be a standard approach to gzip the data in an HTTP
request.

We developed a convention internally of using the ``Content-Encoding:``
header on the HTTP request to ``gzip`` (which mirrors ``Accept-Encoding:`` on
browser requests and the resulting ``Content-Encoding: gzip`` on the response
that follows). This also makes the process transparent to underlying
``Content-Type:`` headers.  Our payloads were JSON but this could easily be
used for XML or any other text-like data.

In testing it also became apparent that very small requests (like small
responses) grow when gzip compressed. It's probably best to put a *minimum*
bound on content lengths that you will compress --  100-150 bytes is
reasonable.

Advantages to using Content-Encoding instead of a custom Content-Type header
is that this will be generally transparent to web frameworks, allowing you
to continue using any out-of-the-box parsers/helpers/etc.

Use At Your Own Risk
====================

Using this bare-minimum code, there's a huge potential for a denial of
service attack since your application server will continue to accept gzip
content until it runs out of memory.

This can potentially be mitigated by configuring the load balancer or
reverse proxy (which will almost inevitably be processing traffic for a
production application server) to limit the HTTP message size, e.g.
Nginx's ``client_max_body_size`` parameter.

Show Me The Code
================

* A reference python_ client
* A reference `C++`_ client
* A minimal Django_ project
* A minimal Flask_ application

.. _python: python/
.. _`C++`: cpp/
.. _Django: django/
.. _Flask: flask/

Testing Locally
===============

Launch one of the servers (instructions in the each directory). This will
start a listener on localhost:9000. Now you can run either of the clients,
which expect to connect to localhost:9000.
