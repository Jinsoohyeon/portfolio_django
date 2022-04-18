from pyexpat import model
from .models import Mail, Memo
from django import forms

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ('content',)

class Mailform(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'address', 'phone', 'message')