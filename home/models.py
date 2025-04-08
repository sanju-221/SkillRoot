from django.db import models

# Create your models here.

class categories(models.Model):
    cat_name = models.CharField(max_length = 150)
    cat_spec = models.CharField(max_length = 250)
