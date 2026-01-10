from django.urls import path

from fruits.views import index_view

urlpatterns = [
    path('', index_view),
]