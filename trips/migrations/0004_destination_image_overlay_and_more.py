# Generated by Django 4.2.5 on 2023-09-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_packagetheme_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='image_overlay',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='destination',
            name='milestone_covered',
            field=models.CharField(default='', max_length=100),
        ),
    ]