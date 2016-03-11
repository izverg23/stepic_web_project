from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model) :
	#id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name='+') 
	likes = models.ManyToManyField(User)
		
	def get_absolute_url(self) :
		return '/question/%d/' % self.id

class Answer(models.Model) :
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
	author = models.ForeignKey(User, related_name='+')
