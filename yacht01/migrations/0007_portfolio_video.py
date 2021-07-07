# Generated by Django 3.2.4 on 2021-07-03 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yacht01', '0006_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='video',
            field=models.FileField(null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm'])]),
        ),
    ]