from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from plot_viewer import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/', include('plot_viewer.urls')),
    path('admin/', admin.site.urls),
]
