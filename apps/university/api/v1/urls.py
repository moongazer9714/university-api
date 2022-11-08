from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, ServiceViewSet, ReasonViewSet, FAQViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'reason', ReasonViewSet)
router.register(r'faq', FAQViewSet)


urlpatterns = [
    path('', include(router.urls))
]
