# Generated by Django 2.2.1 on 2019-09-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('number', models.IntegerField(max_length=13)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=600)),
            ],
        ),
    ]
