# Generated by Django 2.2.1 on 2019-08-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
