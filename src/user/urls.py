from django.urls import include, path
from rest_framework import routers
from .views.user_viewset import UserViewSet
from .views.client_viewset import ClientViewSet
from .views.freelancer_viewset import FreelancerViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'freelancers', FreelancerViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
