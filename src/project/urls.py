from django.urls import path, include
from rest_framework import routers
from .views.project_viewset import ProjectViewSet
from .views.task_viewset import TaskViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
