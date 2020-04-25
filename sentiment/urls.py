from django.urls import path
from . import views
app_name = 'Home'

urlpatterns = [
    path('', views.home, name="index"),
    path('model1', views.model1, name="model1"),
    path('model2', views.model2, name="model2"),
    path('resources', views.resources, name="resources"),
    #path('india/', views.resources, name="india"),
]
