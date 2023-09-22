from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Lesson
from .serializers import LessonSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class LessonsAPI(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(product__name="Yandex").select_related('Product')
    serializer_class = LessonSerializer
    http_method_names = ['get']