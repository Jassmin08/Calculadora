from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.calculadora, name='calculadora'),
    path('admin/', admin.site.urls),
    path('calculadora/', include('calculadora.urls')),
]
