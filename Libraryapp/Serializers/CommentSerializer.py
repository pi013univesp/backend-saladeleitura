from rest_framework import serializers
from Libraryapp.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "forum",
            "name",
            "commentText"
        )
