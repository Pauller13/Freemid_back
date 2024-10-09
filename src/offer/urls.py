from  django.urls import path, include
from rest_framework import routers
from .views.skill_viewset import  SkillViewSet


router = routers.DefaultRouter()
router.register(r'skills', SkillViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
