# Generated by Django 4.0 on 2023-03-30 10:25

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kobita', '0005_user_alter_comment_created_at_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 30, 16, 25, 16, 743366)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 30, 16, 25, 16, 741371)),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
