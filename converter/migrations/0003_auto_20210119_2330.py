# Generated by Django 3.0.4 on 2021-01-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20210119_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imagefile4',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='image',
            name='imagefile5',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='image',
            name='imagefile6',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
