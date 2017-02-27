from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AllModules.as_view(), name='all_modules'),
]
