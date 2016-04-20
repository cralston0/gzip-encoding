C++ Client
----------

A reference client in C++ that demonstrates how to compress and set headers
to transmit gzip'ed data.

This makes use of CPR_ which is a C++ library inspired by Python's Requests_
and the useful GZipCodec_ wrapper.

Building & Running
~~~~~~~~~~~~~~~~~~

    ::
        $ git submodule update --init --recursive
        $ make
        $ ./client


.. _CPR: https://github.com/whoshuu/cpr
.. _Requests: http://docs.python-requests.org/en/master/
.. _GZipCodec: https://github.com/chafey/GZipCodec
