from django.urls import path
from . import views

app_name='sponser'

urlpatterns = [
    path('registerSponser',views.register_sponser, name='register'),
]