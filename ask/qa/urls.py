
from django.conf.urls import url
from django.contrib import admin
from qa.views import test, main_page, popular_page, question_page, ask_page, signup_page, login_page

urlpatterns = [
    url(r'^question/(?P<num>\d+)', question_page, name='question-page'),
    url(r'^popular', popular_page, name='popular-page'),
    url(r'^$', main_page, name='main-page'),
    url(r'^login/', login_page, name='login-page'),
    url(r'^signup/', signup_page, name='sign-up'),
    url(r'^admin/',  admin.site.urls),
    url(r'^ask', ask_page, name='ask-page'),
]
