from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from qa.models import Question, Answer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request) :
	pageLimit = 10
	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
	qwests = Question.objects.all().order_by('-id')
	
	from django.core.paginator import Paginator
	
	page = request.GET.get('page') or 1
	try :
		page = int(page)
	except ValueError :
		page = 1
	paginator = Paginator(qwests, pageLimit)
	paginator.baseurl = '/?page='
	try :
		page = paginator.page(page)
	except EmptyPage :
		page = paginator.page(paginator.num_pages)
	return render(request, 'questionList.html', {
		'title' : 'qwests and answers',
		'list' : page.object_list,
		'paginator' : paginator, 
		'page' : page,
	})
	

def popular(request) :
	pageLimit = 10
	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
	qwests = Question.objects.all().order_by('-likes')
	
	from django.core.paginator import Paginator
	
	page = request.GET.get('page') or 1
	try :
		page = int(page)
	except ValueError :
		page = 1
	paginator = Paginator(qwests, pageLimit)
	paginator.baseurl = '/?page='
	try :
		page = paginator.page(page)
	except EmptyPage :
		page = paginator.page(paginator.num_pages)
	return render(request, 'questionList.html', {
		'title' : 'popular quests',
		'list' : page.object_list,
		'paginator' : paginator, 
		'page' : page,
	})

def question(request, quest_id) :
	try :
		quest = Question.objects.get(id = quest_id)
	except Question.DoesNotExist :
		raise Http404
	answers = Answer.objects.all().filter(question = quest)
	
	title = 'qwest ' + quest_id
	
	user = request.user
	
	if user.is_authenticated() :
		form = AnswerForm(initial={'question' : quest_id})
	
	return render(request, 'question.html', {
		'title' : title,
		'question' : quest,
		'list' : answers,
		'form' : form,
	})

def ask(request) :
	user = request.user
	if request.method == "POST" :
		#print("POST!!!!!!!!!!!!!!!!!!!!!!!!!")
		form = AskForm(request.POST)
		if form.is_valid() :
			if user.is_authenticated() :
				#print("FORM IS VALID!!!!!!!!!!!!")
				form.author = user
				quest = form.save()
				#print("QUEST IS CREATE!!!!!!!!!!")
				url = quest.get_absolute_url()
				#print("URL = " + url +"!!!!!!!!!")
				return HttpResponseRedirect(url)
			else :
				raise Http404
	else :
		form = AskForm()
	return render(request, 'ask_add.html', {
		'form' : form
	})
	
def answer(request) :
	user = request.user
	if request.method == "POST" :
		form = AnswerForm(request.POST)
		if form.is_valid():
			if user.is_authenticated() :
				form.author = user
				answer = form.save()
				url = '/question/' + form.question
				return HttpResponseRedirect(url)
			else :
				raise Http404
			
def signup(request) :
	if request.method == "POST" :
		form = SignupForm(request.POST)
		if form.is_valid() :
			#print("POST!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			#print("username: " + request.POST.get("username") + "!")
			#print("password: " + request.POST.get("password") + "!")
			#print("email: " + request.POST.get("email") + "!")
			form.set_password(request.POST.get("password"))
			user = form.save()
			#print("SAVE USER!!!!!!!!!!!!!!!!!!!!!!!")
			#print("username: " + user.username + " !")
			#print("password: " + user.password + " !")
			#print("email: " + user.email + " !")
			form.loginUser(request)
			return HttpResponseRedirect("/")
	else :
		form = SignupForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})
	
def login(request) :
	if request.method == "POST" :
		form = LoginForm(request.POST)
		if form.is_valid() :
			form.set_password(request.POST.get("password"))
			user = form.loginUser(request)
			return HttpResponseRedirect("/")
	else :
		form = LoginForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})