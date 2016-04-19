from rest_framework.views import APIView
from rest_framework.response import Response


class DrfJsonEchoViewClass(APIView):
    def post(self, request, *args, **kwargs):
        # brute-force compatibility with drf 2.x and 3.x
        try:
            data = request.data
        except AttributeError:
            data = request.DATA

        if data:
            out = {
                'Request Payload': data,
            }
        else:
            out = {
                'Request Payload': '* No data received.',
            }

        return Response(out)
