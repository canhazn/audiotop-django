from blog import models
from rest_framework import serializers



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"
        depth = 1
