from rest_framework import serializers
from .models import BarangModel

class BarangSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangModel
        fields = "__all__"