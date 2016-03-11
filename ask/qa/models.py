from django.db import models
# Create your models here.

class Question(models.Model) :
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name='+') 
	likes = models.ManyToManyField(User)
	
	def get_absolute_url(self) :
		return '/question/%d/' % self.id

class Answer(models.Model) :
	text = models.TextField()
	added_at = models.DateTimeField(blank=True)
	question = models.ForeignKey(Question, related_name='id')
	author = models.ForeignKey(User, related_name='+')