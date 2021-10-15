from django import forms

class RandomForm(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username                                       '}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   