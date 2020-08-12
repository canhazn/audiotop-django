from speaker import models
from rest_framework import serializers


# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Tag
#         fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
        depth = 1
