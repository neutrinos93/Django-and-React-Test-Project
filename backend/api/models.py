from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Foreign key used to link the note to the user
    # So we are linkink the note with the user
    # If we delete the user, all the notes are deleted (cascade)
    # Related name is the field in user table to access their notes
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
