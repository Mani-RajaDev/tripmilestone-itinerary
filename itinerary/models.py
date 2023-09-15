from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from trips.models import Destination


class Itinerary(models.Model):
    destination = models.OneToOneField(
        Destination, on_delete=models.SET_NULL, related_name="itinerary", null=True
    )

    itinerary_details = RichTextUploadingField(null=True, blank=True, default="<div><p></p></div>")

    class Meta:
        verbose_name_plural = "Itineraries"

    def __str__(self):
        return f"{self.destination} Itinerary"
