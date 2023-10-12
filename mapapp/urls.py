from django.urls import path
import mapapp.views

urlpatterns = [
    path('', mapapp.views.main),
    path('adminis/', mapapp.views.index),
    path('add_location/', mapapp.views.add_location, name='add_location'),
    path('update_location/', mapapp.views.update_location, name='update_location'),
    path('delete_location/', mapapp.views.delete_location, name='delete_location'),
]
