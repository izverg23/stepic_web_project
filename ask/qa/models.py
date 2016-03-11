from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model) :
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name='+') 
	likes = models.ManyToManyField(User)
	
	def get_absolute_url(self) :
		return '/question/%d/' % self.pk

class Answer(models.Model) :
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question, related_name='pk')
	author = models.ForeignKey(User, related_name='+')