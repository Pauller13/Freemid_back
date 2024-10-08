from django.urls import include, path
from rest_framework import routers
from .views.user_viewset import UserViewSet
from .views.client_viewset import ClientViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
