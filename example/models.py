from django.db import models

class recepie(models.Model):
    name=models.CharField(max_length=10)
    description=models.TextField()
    image=models.ImageField(upload_to="recepie")

    def __str__(self):
        return self.name
