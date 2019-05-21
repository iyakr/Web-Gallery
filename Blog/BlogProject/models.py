from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from Users.models import Profile
from django.db import models
from PIL import Image

class Post(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='images')
    title = models.CharField(max_length=50)
    text = models.TextField(100)
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.image.path)
        if image.height > 164 or image.width > 164:
            resize = (364, 364)
            image.thumbnail(resize)
            image.save(self.image.path)
    @property
    def get_image_url(self):
        return '/Images/images/{}'.format(self.image)
