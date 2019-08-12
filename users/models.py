from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
import django.conf as settings;


class CustomUser(AbstractUser):
    neighbourhood = models.ForeignKey('neighbour.Neighbourhood', on_delete=models.CASCADE, null=True,)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email = models.CharField(max_length=30)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
        

    
