from django.conf.urls import url

from views import json_echo_view_function, JsonEchoViewClass
# from drf_views import DrfJsonEchoViewClass

urlpatterns = [
    url(r'^$', json_echo_view_function, name='echo'),
    url(r'^alt/$', JsonEchoViewClass.as_view(), name='alt'),
    # url(r'^drf/$', DrfJsonEchoViewClass.as_view(), name='drf'),
]
