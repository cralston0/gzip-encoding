Django
------

A minimal Django project that uses middleware to inflate the gzipped
request body before allowing a view to process the request as normal. For
use in other Django projects, copy the middleware into your own app and add
to `MIDDLEWARE_CLASSES` in settings.

This middleware works the same way when using views from `Django Rest
Framework`_. To test the DRF views in this example, install DRF 2.x or 3.x
and uncomment the two drf-related lines in `urls.py`.

Running
~~~~~~~

To run this server: ::

    $ virtualenv gzip
    $ pip install -r requirements.txt
    $ ./run_me

.. _`Django Rest Framework`: http://www.django-rest-framework.org/
