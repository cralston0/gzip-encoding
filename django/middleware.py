from gzip import GzipFile
import io


def decompress_bytes(b):
    zbuf = io.BytesIO(b)
    decompressed_file = GzipFile(mode='rb', fileobj=zbuf)
    return decompressed_file.read()


class GzipRequestBodyMiddleware(object):
    gzip_content_encoding = 'gzip'

    def process_request(self, request):
        content_encoding = request.META.get('HTTP_CONTENT_ENCODING', '')
        if content_encoding == self.gzip_content_encoding:
            zbuf = io.BytesIO(request.body)
            decompressed_file = GzipFile(mode='rb', fileobj=zbuf)
            new_body = decompressed_file.read()
            request._body = new_body
            # djangorestframework uses the private parameter _stream
            # see: http://stackoverflow.com/questions/22740310/how-to-update-django-httprequest-body-in-middleware
            request._stream = io.BytesIO(new_body)
