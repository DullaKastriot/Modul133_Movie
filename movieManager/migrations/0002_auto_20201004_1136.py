# Generated by Django 3.1.1 on 2020-10-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movieManager'),
        ),
    ]
