from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from qa.models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main_page(request, *args, **kwargs):
    page = int(request.GET.get('page'))
    limit = 10
    questions = Question.objects.new()
    paginator = Paginator(questions, limit)
    if page > paginator.num_pages:
        raise Http404
    page = paginator.page(page)
    paginator.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def popular_page(request, *args, **kwargs):
    page = int(request.GET.get('page'))
    limit = 10
    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)
    if page > paginator.num_pages:
        raise Http404
    page = paginator.page(page)
    paginator.baseurl = '/popular/?page='
    return render(request, 'templates/index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def question_page(request, **kwargs):
    num = int(kwargs.get('num'))
    question = get_object_or_404(Question, id=num)
    return render(request, 'templates/question.html', {
        'question': question,
        'answers': Answer.objects.filter(question=question).all()
    })
