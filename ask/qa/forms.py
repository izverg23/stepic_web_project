from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from qa.models import Question, Answer

class AskForm(forms.Form) :
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	author = 1
	
	def clean_title(self) :
		title = self.cleaned_data['title']
		return title

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def save(self) :
		quest = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=self.author)
		#quest.save()
		return quest
	
class AnswerForm(forms.Form) :
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)
	author = 1
	
	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def clean_question(self) :
		try :
			quest_id = int(self.cleaned_data['question'])
		except ValueError :
			raise forms.ValidationError('fail input')
		return quest_id
	
	def save(self) :
		answer = Answer.objects.create(text=self.cleaned_data['text'], question=self.cleaned_data['question'], author=self.author)
		#answer.save()
		return answer
		
class SignupForm(forms.Form) :
	username = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_email(self) :
		email = self.cleaned_data['email']
		return email
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def save(self) :
		user = User.objects.create_user(self.clean_username(), self.clean_email(), self.clean_password())
		user.save()
		return user
	
	def loginUser(self, request) :
		user = authenticate(username=self.clean_username(), password=self.clean_password())
		login(request, user)
		return user
		
class LoginForm(forms.Form) :
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def loginUser(self, request) :
		user = authenticate(username=self.clean_username(), password=self.clean_password())
		login(request, user)
		return user