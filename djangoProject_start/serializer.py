from rest_framework import serializers

from djangoProject_start import  models

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
