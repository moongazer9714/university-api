from rest_framework import serializers
from ...models import About, Service, Reason, FAQ


# class AboutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = About
#         fields = '__all__'
#
#
# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'
#
#
# class ReasonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reason
#         fields = '__all__'
#
#
# class FAQSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FAQ
#         fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'

    def set_model(self, model):
        self.Meta.model = model
