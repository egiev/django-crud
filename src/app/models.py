from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	publish_date = models.DateTimeField('Date published')
	content = models.CharField(max_length=200)

	def __str__(self):
		return self.title


class Comments(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
	text = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
	publish_date = models.DateTimeField('Date Published')

	def __str__(self):
		return self.text
