# Generated by Django 4.0 on 2023-03-30 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobita', '0004_remove_post_like_alter_comment_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=15)),
                ('unique_id', models.UUIDField()),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 30, 16, 20, 43, 933621)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 3, 30, 16, 20, 43, 933621)),
        ),
    ]
