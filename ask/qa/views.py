from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.forms import AskForm, AnswerForm
import logging

from qa.models import Question, Answer

logger = logging.getLogger(__name__)

@require_GET
def test(request, *args, **kwargs):
    logger = logging.getLogger(__name__)
    logger.debug('test')
    return HttpResponse('OK')

@require_GET
def main_page(request, *args, **kwargs):
    logger = logging.getLogger(__name__)
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
        'paginator': paginator,
        'page': page
    })


def question_page(request, **kwargs):
    logger = logging.getLogger(__name__)
    logger.debug('question_page')

    num = int(kwargs.get('num'))
    question = get_object_or_404(Question, id=num)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            logger.debug(f"url: {url}")
            return HttpResponseRedirect(url)
    else:

        form = AnswerForm(initial={'question': question.pk})
        return render(request, 'question.html', {
            'question': question,
            'title': question.title,
            'answers': Answer.objects.filter(question=question)[:],
            'form': form,
        })

@require_GET
def popular_page(request, *args, **kwargs):
    logger = logging.getLogger(__name__)
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

def ask_page(request, *args, **kwargs):
    logger = logging.getLogger(__name__)
    logger.debug('ask_page')
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask.html', {'form': form})


# form = AnswerForm(initial={'question': question_id})
