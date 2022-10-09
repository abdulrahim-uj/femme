from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('redirect-test/', views.test, name="test_redirect"),
]

app_name = "web"
