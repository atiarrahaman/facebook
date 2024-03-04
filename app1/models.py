from django.db import models

# Create your models here.



# Hunt Models 

class Hunting(models.Model):
    username= models.CharField(max_length=250)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username
    