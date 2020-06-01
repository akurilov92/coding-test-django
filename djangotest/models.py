from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    birthday = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return str({
            'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'birthday': self.birthday
        })
