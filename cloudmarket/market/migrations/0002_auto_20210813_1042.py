# Generated by Django 3.2.5 on 2021-08-13 01:42

import django.core.validators
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to='img/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000000)]),
        ),
    ]