import json

from flask import request
from flask.views import MethodView


class JsonEchoViewClass(MethodView):
    def post(self):
        data = request.get_json()
        out = 'Request Payload:\n'
        if data:
            out += json.dumps(data, indent=2)
        else:
            out += ' * No data received.'
        out += '\n'
        return out


def json_echo_view_function():
    data = request.get_json()
    out = 'Request Payload:\n'
    if data:
        out += json.dumps(data, indent=2)
    else:
        out += ' * No data received.'
    out += '\n'
    return out
