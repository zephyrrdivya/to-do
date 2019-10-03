from django.urls import include, path
from rest_framework import routers, renderers
# from django.views.decorators.csrf import csrf_exempt

from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.api_root),
    path('', include(router.urls)),
]
