from django.urls import path

from .views import user_list


urlpatterns = [
    path(r'^$', user_list, name='user_list'),
]
