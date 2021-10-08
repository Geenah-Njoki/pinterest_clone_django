from django import forms

class RandomForm(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()
