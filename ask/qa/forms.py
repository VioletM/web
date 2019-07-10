from django import forms
from qa.models import Question, Answer

class AskForm(forms.ModelForm):

    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        question = Question(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author_id=1)
        question.save()
        return question

class AnswerForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        pass

    def save(self):
        answer = Answer(text=self.cleaned_data['text'], question=self.cleaned_data['question'], author_id=1)
        answer.save()
        return answer