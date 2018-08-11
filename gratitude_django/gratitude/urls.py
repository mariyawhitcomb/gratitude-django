from django.urls import path
from .views import current_user, UserList, entries_list, entry_detail

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('entries/<int:pk>', entries_list, name='entries_list'),
    path('entries/<int:pk>/<date>', entry_detail, name='entry_detail')
]



 