from django.urls import path
from extractor_app.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
