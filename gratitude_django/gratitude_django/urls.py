
from django.conf.urls import include, url
from django.contrib import admin
from gratitude.resources import EntryResource
from rest_framework_jwt.views import obtain_jwt_token


from django.urls import path

entry_resource = EntryResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gratitude/', include(entry_resource.urls)),
    path('token-auth/', obtain_jwt_token),
    path('gratitude/', include('gratitude.urls')),
]
