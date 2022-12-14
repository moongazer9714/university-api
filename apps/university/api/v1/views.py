from rest_framework import viewsets, permissions
# from .serializers import AboutSerializer, ServiceSerializer, ReasonSerializer, FAQSerializer
from .serializers import UniversitySerializer
from ...models import About, Service, Reason, FAQ


class AboutViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/university/v1/about/<id>/
    queryset = About.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(About)
        return serializer


class ServiceViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/university/v1/service/<id>/
    queryset = Service.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(Service)
        return serializer


class ReasonViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/university/v1/reason/<id>/
    queryset = Reason.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(Reason)
        return serializer


class FAQViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/api/university/v1/faq/<id>/
    queryset = FAQ.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        UniversitySerializer().set_model(FAQ)
        return serializer
