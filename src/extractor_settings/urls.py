from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect


urlpatterns = [
    path('', include('extractor_app.urls')),
    path('', include('auth_handler.urls')),
    path('', include('session_handler.urls')),
    path('admin/', admin.site.urls),
    path('', lambda r: HttpResponseRedirect('extract/'))
]

handler404 = 'extractor_app.views.handler404'
handler500 = 'extractor_app.views.handler500'
