from django.urls import include, path
from rest_framework import routers

from other.views.conversation_viewset import ConversationViewSet
from other.views.message_viewset import MessageViewSet
from other.views.rating_viewset import RatingViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ratings', RatingViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
