from django.db import models

class Projects(models.Models):
    image = models.ImageField(upload_to='images/')
    descripton = models.TextField(max_length=255)
    link = models.TextField(max_length=255)
