# from django import urls
# from django.conf.urls import url
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# from django.db.models.fields import URLField


class User(AbstractUser):
	pass

	def __str__(self):
		return self.username
	

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	thumbnail = models.ImageField()
	publish_date = models.TimeField(auto_now_add=True)
	last_updated = models.TimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField()

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("detail", kwargs={
			'slug': self.slug
		})

	@property
	def get_comment_count(self):
		return self.comment_set.all().count()

	@property
	def get_view_count(self):
		return self.postview_set.all().count()

	@property
	def get_like_count(self):
		return self.like_set.all().count()

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	timestamp = models.TimeField(auto_now_add=False)
	content = models.TextField()

	def __str__(self):
		return self.user.username


class PostView(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	timestamp = models.TimeField(auto_now_add=False)

	def __str__(self):
		return self.user.username


class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username
