
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, main_page, popular_page, question_page, ask_page

urlpatterns = [
    url(r'^question/(?P<num>\d+)', question_page, name='question-page'),
    url(r'^popular', popular_page, name='popular-page'),
    url(r'^$', main_page, name='main-page'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^admin/',  admin.site.urls),
    url(r'^ask', ask_page, name='ask-page'),
]
