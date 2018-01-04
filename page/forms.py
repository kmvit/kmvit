from django import forms
from .views import *
from .models import *

class FeedBackAdd(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
