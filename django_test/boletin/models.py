from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

