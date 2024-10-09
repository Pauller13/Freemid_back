from django.urls import path, include
from rest_framework import routers
from .views.project_viewset import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
     path('project/', include(router.urls)),
]
