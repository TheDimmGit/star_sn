# Generated by Django 4.2.6 on 2023-10-23 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='TITLE', max_length=100)),
                ('content', models.TextField(db_column='CONTENT')),
                ('date', models.DateTimeField(auto_now_add=True, db_column='DATE')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=255)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='PostTagRelations',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('post', models.ForeignKey(db_column='POST', on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('tag', models.ForeignKey(db_column='TAG', on_delete=django.db.models.deletion.CASCADE, to='post.tag')),
            ],
            options={
                'db_table': 'post_tag_relations',
            },
        ),
    ]
