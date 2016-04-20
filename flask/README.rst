Flask Application
-----------------

A minimal Flask application that uses ``before_request`` to inflate the
gzipped request data before allowing a view to process the request as
normal. For use in other Flask applications, copy the middleware into your
own app and register it with ``app.before_request()`` or the
``@app.before_request`` decorator.

Running
~~~~~~~

To run this server: ::

    $ virtualenv gzip
    $ pip install -r flask/requirements.txt
    $ python flask/run_me.py

