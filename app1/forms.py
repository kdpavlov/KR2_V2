from django import forms
from .models import StudyRecord

class StudyRecordForm(forms.ModelForm):
    class Meta:
        model = StudyRecord
        fields = ['name', 'course', 'score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название курса'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Баллы'}),
        }
        labels = {
            'name': 'Имя',
            'course': 'Курс',
            'score': 'Баллы'
        }