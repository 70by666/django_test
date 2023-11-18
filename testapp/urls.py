from django.urls import path

from testapp.views import testapp

urlpatterns = [
    path('', testapp)
]
