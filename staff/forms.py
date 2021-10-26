from django import forms
from django.db.models.fields import TextField

class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, widget= forms.HiddenInput)
    recipient = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)