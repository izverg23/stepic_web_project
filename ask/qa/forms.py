from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form) :
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	
	def clean_title(self) :
		title = self.cleaned_data['title']
		return title

	def clean_text(self) :
		text = self.cleaned_data['text']
		return text
		
	def save(self) :
		quest = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
		#quest.save()
		return quest
	
class AnswerForm(forms.Form) :
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)
	
	#def __init__(self, *args, **kwargs) :
	#	super(AnswerForm, self).__init__(*args, **kwargs)
	
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
		answer = Answer.objects.create(text=self.cleaned_data['text'], question=self.cleaned_data['question'])
		#answer.save()
		return answer