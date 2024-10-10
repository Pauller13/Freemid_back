from django.urls import include, path
from rest_framework import routers

from other.views.conversation_viewset import ConversationViewSet
from other.views.message_viewset import MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
