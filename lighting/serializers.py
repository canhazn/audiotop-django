from lighting import models
from rest_framework import serializers



class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produkt
        fields = "__all__"
        depth = 1
