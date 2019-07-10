from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
import logging

from qa.models import Question, Answer

logger = logging.getLogger(__name__)

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def main_page(request, *args, **kwargs):
    logger.debug('main_page')
    page = int(request.GET.get('page', 1))
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

@require_GET
def popular_page(request, *args, **kwargs):
    logger.debug('popular_page')
    page = int(request.GET.get('page'))
    limit = 10
    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)
    if page > paginator.num_pages:
        raise Http404
    page = paginator.page(page)
    paginator.baseurl = '/popular/?page='
    return render(request, 'index.html', {
        'paginator': paginator,
        'page': page
    })

@require_GET
def question_page(request, **kwargs):
    logger.debug('question_page')
    num = int(kwargs.get('num'))
    question = get_object_or_404(Question, id=num)
    print(question.title)
    return render(request, 'question.html', {
        'question': question,
        'title': question.title,
        'answers': Answer.objects.filter(question=question)[:]
    })
