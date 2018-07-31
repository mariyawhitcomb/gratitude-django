from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views





urlpatterns = [
    url('entry', views.entry_list, name='entry_list'),
    # url(r'entries/$', views.EntryList.as_view(), name='entries-list'),
    # url(r'entries/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view(), name='entry-detail'),
]