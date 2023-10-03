from django.urls import path
import mapapp.views

urlpatterns = [
    path('', mapapp.views.index),
]
