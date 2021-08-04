# Generated by Django 3.2.5 on 2021-08-04 00:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0004_merge_0002_alter_post_image_0003_auto_20210802_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='used_id',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='used_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userid_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]