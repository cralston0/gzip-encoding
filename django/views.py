import json

from django.http import HttpResponse
from django.views.generic import View


class JsonEchoViewClass(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        out = 'Request Payload:\n'
        if data:
            out += json.dumps(data, indent=2)
        else:
            out += ' * No data received.'
        out += '\n'

        return HttpResponse(out)


def json_echo_view_function(request):
    data = json.loads(request.body)

    out = 'Request Payload:\n'
    if data:
        out += json.dumps(data, indent=2)
    else:
        out += ' * No data received.'
    out += '\n'

    return HttpResponse(out)
