from django.urls import path
from .views import home, demo_eval

urlpatterns = [
    path('', home, name='home'),
    path('demo-eval/', demo_eval, name='demo_eval'),
]