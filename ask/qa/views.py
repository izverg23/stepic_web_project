from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request) :
	pageLimit = 10
	#Entry.objects.order_by(Coalesce('summary', 'headline').desc()) #asc()
	qwests = Question.objects.all().order_by('-added_at')
	
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
	return render(request, '/template/questionList.html', {
		'title' : 'Вопросы и ответы',
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
	return render(request, '/template/questionList.html', {
		'title' : 'Популярные вопросы',
		'list' : page.object_list,
		'paginator' : paginator, 
		'page' : page,
	})

def question(request, id) :
	try :
		quest = Question.objects.get(id = id)
	except Question.DoesNotExit :
		raise Http404
	answers = quest.Answer.all() #Answer.objects.all().filter(question = quest)
	return render(request, '/template/question.html', {
		'title' : 'Вопрос №' + id,
		'question' : quest,
		'list' : answers,
	})