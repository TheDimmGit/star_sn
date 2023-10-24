from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    self = serializers.HyperlinkedIdentityField(view_name='post-detail')
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, post_object):
        return post_object.like_counter

    def update(self, instance, validated_data):
        post_author = instance.author
        current_user = self.context['request'].user
        if post_author != current_user:
            raise serializers.ValidationError('Post can be edited only by author')
        return super().update(instance, validated_data)

    class Meta:
        model = Post
        fields = ('id', 'self', 'author', 'title', 'content', 'date', 'likes_count')
