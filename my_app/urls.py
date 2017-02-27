from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListCreateModule.as_view(), name='all_modules'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyModule.as_view(), name='rud_modules'),
]
