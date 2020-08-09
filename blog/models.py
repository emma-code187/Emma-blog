from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model): 
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	featured = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk}) 
		
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created_date']


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
