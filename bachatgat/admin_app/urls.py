from django.urls import path
from . import views

urlpatterns = [
    path('app_admin/', views.admin_app, name='admin_app'),
]