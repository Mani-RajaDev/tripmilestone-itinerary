# Generated by Django 4.2.5 on 2023-09-12 15:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0002_alter_packagetheme_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary_details', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('destination', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itinerary', to='trips.destination')),
            ],
            options={
                'verbose_name_plural': 'Itineraries',
            },
        ),
    ]
