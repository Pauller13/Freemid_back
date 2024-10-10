from django.urls import include, path
from rest_framework import routers
from .views.user_viewset import UserViewSet
from .views.client_viewset import ClientViewSet
from .views.freelancer_viewset import FreelancerViewSet
from .views.profil_view import (
    get_current_user_profile,
    get_clients_profiles,
    get_freelancers_profiles,
    get_client_profile_by_id,
    get_freelancer_profile_by_id
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'freelancers', FreelancerViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('profile/', get_current_user_profile, name='current_user_profile'), 
    path('client/', get_clients_profiles, name='profile_client'),
    path('client/<int:id>/', get_client_profile_by_id, name='profile_client_id'),          
    path('freelancer/', get_freelancers_profiles, name='profile_freelancers'),
    path('freelancer/<int:id>/', get_freelancer_profile_by_id, name='profile_freelancer_id')
]
