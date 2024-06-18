from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def print(self,name):
        return self.name
