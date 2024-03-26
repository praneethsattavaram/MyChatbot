from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  models = models.TextField()
  message = models.TextField()
  create_at = models.DataTimeField(auto_now_add = True)

  def __str__(self):
    return f'{self.user.username} : {self.message}'
