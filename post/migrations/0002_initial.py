# Generated by Django 4.2.6 on 2023-10-23 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(db_column='AUTHOR', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='author',
            field=models.ForeignKey(db_column='AUTHOR', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(db_column='POST', on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AlterUniqueTogether(
            name='posttagrelations',
            unique_together={('tag', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('author', 'post')},
        ),
    ]
