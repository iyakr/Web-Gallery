from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
class User(models.Model):
    roles = models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')

    def __str__(self):
        return self.img.name

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        if image.height>164 or image.width>164:
            resize = (364, 364)
            image.thumbnail(resize)
            image.save(self.img.path)

    @property
    def get_avatar_url(self):
        if self.img:
            return '/Images/user_images/{}'.format(self.img)
        else:
            return '/Images/default.jpg'
