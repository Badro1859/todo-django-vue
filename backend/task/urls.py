# django packages
from django.urls import path, include

# rest packages
from rest_framework import routers

# local packages
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

