from django.db import models
from django .contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=264,blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-upload_date']

class Like(models.Model):
    post = models.ForeignKey(Post,related_name='liked_post',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='liker',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} : {}'.format(self.user, self.post)



