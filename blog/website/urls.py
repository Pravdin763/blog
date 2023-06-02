from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view())]