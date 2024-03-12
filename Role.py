from django.db import models

class Role(models.Model):
    libelle = models.CharField(max_length=50)