from django.urls import path
from . import views

# Add namespace tu URLconfs 
app_name = 'polls' 
urlpatterns = [
    # route: URL pattern; first match is picked
    # view: when a pattern is matched, a VIEW function is called
    # w/ an HttpRequest obj as argument [+ captured values captures from the route, as KW arguments]
    # [kwargs]: Arbitrary KW args passed to the view
    # [name]: Unambiguous name for the URL, can be used in templates e.g.

    # /polls/
    # Traditional way: 
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # /polls/5/
    # The traditional way
    # path('<int:question_id>/', views.detail, name='detail'),
    # One can change the structure of the URL, without breaking the links (loosely-coupling)
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # Amending URLconf for generic view:
    # The DetailView generic view expects the PK to be retrieved from the URL
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),


    # /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # Amending URLconf for generic view
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

