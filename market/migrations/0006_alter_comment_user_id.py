# Generated by Django 3.2.5 on 2021-08-04 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0005_auto_20210804_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userid_comment', to='auth.user'),
            preserve_default=False,
        ),
    ]