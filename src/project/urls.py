from django.urls import path, include
from rest_framework import routers
from .views.project_viewset import ProjectViewSet
from .views.task_viewset import TaskViewSet
from .views.deliverable_viewset import DeliverableViewSet
from .views.payment_viewset import PaymentModel, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'deliverables', DeliverableViewSet)
router.register(r'payment', PaymentViewSet)
urlpatterns = [
     path('', include(router.urls)),
]
