from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        """定义元数据,指定显示内容"""
        model=Topic
        fields=['text']
        labels={'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}