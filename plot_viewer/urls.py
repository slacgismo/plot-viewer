from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'plot_viewer'
urlpatterns = [
    path('home', views.modelListView.as_view(template_name="home.html"),name = 'home'),
]
