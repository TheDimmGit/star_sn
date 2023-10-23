from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    self = serializers.HyperlinkedIdentityField(view_name='post-detail')
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post_object):
        return post_object.like_counter

    class Meta:
        model = Post
        fields = ('id', 'self', 'author', 'title', 'content', 'date', 'likes_count')
