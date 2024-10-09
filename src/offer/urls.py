from  django.urls import path, include
from rest_framework import routers
from .views.offer_viewset  import OfferViewSet
from .views.offerskill_viewset import OfferSkillViewSet
from .views.proposal_viewset import ProposalViewSet
from .views.skill_viewset import  SkillViewSet
from ..other.urls import router

router = routers.DefaultRouter()
router.register(r'offers', OfferViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'proposals', ProposalViewSet)
router.register(r'offerskills', OfferSkillViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
