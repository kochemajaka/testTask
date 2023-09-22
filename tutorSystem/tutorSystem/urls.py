from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path("", include("tutor.urls")),
    path("admin/", admin.site.urls),
]
