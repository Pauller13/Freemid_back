from django.urls import include, path
from rest_framework import routers

from other.views.conversation_viewset import ConversationViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
