from django import forms
from .views import *
from .models import *
from captcha.fields import CaptchaField

class FeedBackAdd(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    captcha = CaptchaField()
    
