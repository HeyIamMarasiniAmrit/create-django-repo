from django import forms

# Change 'form' to 'Form'
class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(initial="")
    city = forms.CharField()
    email = forms.EmailField()


class Login(forms.Form):
    city = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    key=forms.CharField(widget=forms.HiddenInput())

    # File and url
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()



class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state= forms.CharField()
    pin_code = forms.IntegerField()
    agree_terms = forms.NullBooleanField()