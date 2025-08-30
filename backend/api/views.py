from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# This view will list all the notes created by the users and will create a new one
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # Specify what we get - overrides queryset
    def get_queryset(self):
        # get the user that sent the request
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # Override the create method of this class
    def perform_create(self, serializer):
        if serializer.is_valid():
            # Save by adding author since it's read only
            serializer.save(author=self.request.user)
        else:
            print(serializer.user)

# View to delete note
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # Specify what we get - overrides queryset
    def get_queryset(self):
        # get the user that sent the request
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    # List of objects to consider when creating a new one, to
    # make sure we don't create a user that already exists
    queryset = User.objects.all()
    # What data we need to create a new user
    serializer_class = UserSerializer
    # Who can call this? Anyone, even if not authenticated
    permission_classes = [AllowAny]