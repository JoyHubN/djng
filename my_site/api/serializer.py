from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'author', 
            'title', 
            'text', 
            'pub_date'
        )

    def get_author(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'