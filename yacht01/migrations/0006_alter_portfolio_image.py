# Generated by Django 3.2.4 on 2021-07-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yacht01', '0005_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='portfolio/'),
        ),
    ]
