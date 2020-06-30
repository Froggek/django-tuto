from django.urls import path
from . import views

urlpatterns = [
    # route: URL pattern; first match is picked
    # view: when a pattern is matched, a VIEW function is called
    # w/ an HttpRequest obj as argument [+ captured values captures from the route, as KW arguments]
    # [kwargs]: Arbitrary KW args passed to the view
    # [name]: Unambiguous name for the URL, can be used in templates e.g.
    path('', views.index, name='index')
]
