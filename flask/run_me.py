#!/usr/bin/env python
from flask import Flask

from middleware import gzip_http_request_middleware
from views import json_echo_view_function, JsonEchoViewClass

app = Flask(__name__)

# this can also be done using the @app.before_request decorator
app.before_request(gzip_http_request_middleware)
app.add_url_rule('/', 'echo', json_echo_view_function, methods=['POST', ])
app.add_url_rule('/alt/', view_func=JsonEchoViewClass.as_view('alt'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='9000')
