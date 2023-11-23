from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_identity = models.TextField()
    sexual_orientation = models.TextField()
    # note = models.TextField()
    
    # def __str__(self):
    #     return self.user.username

