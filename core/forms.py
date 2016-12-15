from django import  forms


class RegForm(forms.Form):
    login = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    about_me = forms.CharField(max_length=1023)
    love_lang = forms.CharField(max_length=1023)