from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField()
    publish=models.DateField()
    cover=models.ImageField(upload_to="cover")
