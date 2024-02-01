from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("foundation_backend.example_app.urls"), name="example_app"),
]

print(settings.DEBUG)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls), name="debug_toolbar"),
    ] + urlpatterns
