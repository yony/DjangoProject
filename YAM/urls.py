from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.site_names, name='site-names'),
]
