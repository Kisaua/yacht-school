# Generated by Django 3.2.4 on 2021-07-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yacht01', '0002_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='yacht/static/img/portfolio/'),
        ),
    ]