# Generated by Django 4.2.6 on 2023-10-23 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_change_reference_user_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_column='DATE', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
