The code for compressing text is from Django's `utils.text.compress_string()` and
`...compress_sequence()` <https://github.com/django/django/blob/master/django/utils/text.py> which
are themselves based on Alan Kennedy's blog post about HTTP compression in Jython
<http://jython.xhaus.com/http-compression-in-python-and-jython/#gzip>

C++ gzip code is from chafey's "C++ GZip Codec" <https://github.com/chafey/GZipCodec>

