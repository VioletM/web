import datetime as dt
import logging

from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from qa.forms import AskForm, AnswerForm, RegistrationForm, LoginForm
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


@csrf_exempt
def question_page(request, **kwargs):
    logger = logging.getLogger(__name__)
    logger.debug('question_page')

    num = int(kwargs.get('num'))
    question = get_object_or_404(Question, id=num)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = AnswerForm(request.POST)
            form._user = request.user
            if form.is_valid():
                answer = form.save()
                url = question.get_url()
                logger.debug('url: {}'.format(url))
                newform = AnswerForm(initial={'question': question.pk})
                return render(request, 'question.html', {
                    'question': question,
                    'title': question.title,
                    'answers': Answer.objects.filter(question=question)[:],
                    'form': newform,
                })
        else:
            return HttpResponseRedirect('/login/')
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
        if request.user.is_authenticated:
            form = AskForm(request.POST)
            if form.is_valid():
                question = form.save()
                url = question.get_url()
                return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/login/')
    else:
        form = AskForm()
        return render(request, 'ask.html', {'form': form})


def signup_page(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
        return render(request, 'signup.html', {'form': form})


def login_page(request, *args, **kwargs):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.save()
            user = authenticate(username=username, password=password)
            logger.debug('user: {}'.format(user))
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect('/')
                response.set_cookie('sessid', request.session.session_key, expires=dt.datetime.now() + dt.timedelta(days=5))
                return response
            else:
                error = u'Wrong password or username'
    form = LoginForm()
    return render(request, 'login.html', {'error': error, 'form': form})
