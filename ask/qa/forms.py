from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class AskForm(forms.Form):

    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        try:
            user = User.objects.get(username='first_user')
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = User(username='first_user')
            user.is_staff = True
            user.is_superuser = True
            user.save()
        question = Question(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author=user)
        question.save()
        return question

class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        pass

    def save(self):
        try:
            user = User.objects.get(username='first_user')
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = User(username='first_user')
            user.is_staff = True
            user.is_superuser = True
            user.save()
        question = get_object_or_404(Question, id=self.cleaned_data['question'])
        answer = Answer(text=self.cleaned_data['text'], question=question, author=user)
        answer.save()
        return answer