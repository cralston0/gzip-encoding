import gzip
import io

from flask import request


def gzip_http_request_middleware():
    encoding = request.headers.get('content-encoding', '')
    if encoding == 'gzip':
        gz = request.get_data()
        zb = io.BytesIO(gz)
        zf = gzip.GzipFile(fileobj=zb)
        clear = zf.read()
        request._cached_data = clear
