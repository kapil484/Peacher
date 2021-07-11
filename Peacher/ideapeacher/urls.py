from django.urls import path
from . import views

app_name='ideapeacher'

urlpatterns = [
    path('register/',views.register_user, name='register_form'),
    path('login/',views.login_user,name='login_form'),
]