from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to = 'profile_pics')

    def __str__(self):
        return "{}'s Profile".format(self.user.username)
