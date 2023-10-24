from django.db import models

from user.models import User


class Post(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    author = models.ForeignKey(
        User,
        db_column='AUTHOR',
        on_delete=models.CASCADE
    )
    title = models.CharField(db_column='TITLE', max_length=100)
    content = models.TextField(db_column='CONTENT')
    date = models.DateTimeField(db_column='DATE', auto_now_add=True)

    @property
    def like_counter(self) -> int:
        return Like.objects.filter(post=self).count()

    @property
    def users_liked(self) -> models.QuerySet:
        return User.objects.filter(like__post=self)

    class Meta:
        db_table = 'post'


# class Tag(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)
#     name = models.CharField(db_column='NAME', max_length=255)
#
#     @property
#     def all_tag_posts(self) -> models.QuerySet:
#         return Post.objects.filter(posttagrelations__tag=self)
#
#     @staticmethod
#     def all_tags_posts(tags: list) -> models.QuerySet:
#         return Post.objects.filter(posttagrelations__tag__in=tags)
#
#     class Meta:
#         db_table = 'tag'
#
#
# class PostTagRelations(models.Model):
#     id = models.AutoField(db_column='ID', primary_key=True)
#     post = models.ForeignKey(Post, db_column='POST', on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, db_column='TAG', on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'post_tag_relations'
#         unique_together = ('tag', 'post')


class Like(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    author = models.ForeignKey(
        User,
        db_column='AUTHOR',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        db_column='POST',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(db_column='DATE', auto_now_add=True)

    class Meta:
        db_table = 'like'
        unique_together = ('author', 'post')
