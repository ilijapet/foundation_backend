import logging

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("foundation_backend.example_app.urls"), name="example_app"),
]
