from django.db import models

class Project(models.Model):
    # by default Django will create auto-increment id
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    date_built = models.DateField()

    def __str__(self):
        return self.title
