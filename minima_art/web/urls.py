from django.urls import path
from .views import home,feedback_view

urlpatterns = [
    path('',home, name="home"),
    path('feedback/', feedback_view, name='feedback'),
]