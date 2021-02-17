from django import forms
from .models import Notice


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'body', 'exp_date']
        widgets = {
            'exp_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }
