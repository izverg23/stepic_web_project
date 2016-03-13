from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form) :
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	author = forms.CharField(widget=forms.HiddenInput)
	
	def clean_title(self) :
		title = self.cleaned_data['title']
		return title

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def save(self) :
		quest = Question(title=self.title, text=self.text, author=self.author)
		quest.save()
		return quest
	
class AnswerForm(forms.Form) :
	text = forms.CharField(widget=forms.Textarea)
	question = forms.CharField(widget=forms.HiddenInput)
	author = forms.CharField(widget=forms.HiddenInput)
	
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
		answer = Answer(text=self.text, question=self.question, author=self.author)
		answer.save()
		return answer