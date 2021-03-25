from django.db import models

# Create your models here
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Slider(BaseModel):
    slider_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='sliders/')
    is_publish = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
    def __str__(self):
        return self.slider_name
