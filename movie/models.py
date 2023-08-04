from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class MOvie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='movie/images/')
    url=models.URLField(blank=True)

class Review(models.Model):
    text=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(MOvie,on_delete=models.CASCADE)
    watchAgain=models.BooleanField()    

    def __str__(self):
        return self.text
def __str__(self):
    return self.title    
