from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author=self._user)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        pass

    def save(self):
        question = get_object_or_404(Question, id=self.cleaned_data['question'])
        answer = Answer(text=self.cleaned_data['text'], question=question, author=self._user)
        answer.save()
        return answer


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=250)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        pass

    def save(self):
        user = User(username=self.cleaned_data['username'], email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        pass

    def save(self):
        return self.cleaned_data['username'], self.cleaned_data['password']