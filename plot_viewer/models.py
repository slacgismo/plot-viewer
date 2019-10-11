from django.db import models
from datetime import datetime
from django.conf import settings

class plot(models.Model):

    image_name = models.CharField(max_length=50, default="", blank=False, unique=True)
    mix_type = models.CharField(max_length=16, default="", blank=False)
    normalization = models.CharField(max_length=30, default="", blank=False)
    season = models.CharField(max_length=6, default="", blank=False)
    location = models.CharField(max_length=30, default="", blank=False)
    model_img_url = models.CharField(max_length=150, default="", blank=False)
    csv_url = models.CharField(max_length=150, default="", blank=False)


    class Meta:
        ordering = ["-location"]

    def __str__(self):
        return self.location
