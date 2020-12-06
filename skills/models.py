from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=150)
    image_tag = models.CharField(max_length=150)

    def __str__(self):
        return self.title
