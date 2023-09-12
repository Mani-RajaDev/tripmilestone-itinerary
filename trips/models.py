from django.db import models

from base.utils import rename_uploaded_file

class PackageTheme(models.Model):
    STATUS = [
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    ]

    theme = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to=rename_uploaded_file)
    status = models.CharField(max_length=10, choices=STATUS)

    @property
    def image_upload_folder(self):
        return "package-images/"

    def __str__(self):
        return self.theme.title()
    

class PackageType(models.Model):
    type_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.type_name.title()


class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    package_theme = models.ForeignKey(PackageTheme, on_delete=models.SET_NULL,  related_name="destinations_theme", null=True)
    package_type = models.ForeignKey(PackageType, on_delete=models.SET_NULL,  related_name="destinations_type", null=True)
    image = models.ImageField(upload_to=rename_uploaded_file)
    nights = models.PositiveIntegerField()
    number_of_hotels = models.PositiveIntegerField() 
    stay_mode = models.CharField(max_length=50)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def image_upload_folder(self):
        return "destination-images/"