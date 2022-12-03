from django.urls import path

from .views import user_list, log_in, log_out, sign_up


urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('login/', log_in, name='log_in'),
    path('logout/', log_out, name='log_out'),
    path('signup/', sign_up, name='sign_up'),
]
