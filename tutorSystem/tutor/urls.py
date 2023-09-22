from django.urls import path, include
from rest_framework import routers


from . import views
from .views import LessonsAPI

router = routers.DefaultRouter()
router.register(r'api/lessons', LessonsAPI)

urlpatterns = [
    path("", views.index, name="index"),
    path("", include(router.urls)),
]