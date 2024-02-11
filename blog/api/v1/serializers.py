from rest_framework import serializers

from blog.models import Category, Comment, Post


class PostSerializer(serializers.ModelSerializer):
    """
    class PostSerializer is for serializing posts
    """

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "category",
            "status",
            "published_date",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    class CategorySerializer is for serializing categories.
    """

    class Meta:
        model = Category
        fields = "__all__"
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    """
    class CommentSerializer is for serializing Comment.
    """

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'name',
            'email',
            'approved',
            'created_date',
            'updated_date',
        ]