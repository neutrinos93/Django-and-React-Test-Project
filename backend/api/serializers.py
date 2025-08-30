from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Built into Django
        # Fields that we want to serialise when new user is accepted or retunrned
        fields = ["id", "username", "password"]
        # Tells Django we want to receive password, but not return it
        extra_kwargs = {"password": {"write_only": True}}

    # Method to be called when new user needs to be created
    # validated_data is data that has already passed Serialisers checks
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        # The author is manually set based on the creator
        extra_kwargs = {"author": {"read_only": True}}