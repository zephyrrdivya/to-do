from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# from .views import home, done_task
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
