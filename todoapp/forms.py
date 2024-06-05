from django.forms import ModelForm
from django import forms

from todoapp.models import Todo
from projectapp.models import Project


class TodoCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height : auto;'}))

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False) #1,2,3,4 안골라도 제출되게하는 코드
    class Meta:
        model = Todo
        fields = ['title','image', 'content', 'priority']