from django.urls import path
from . import views


urlpatterns = [
    path('session/<sessionid>/', views.user_session, name='session'),
]
