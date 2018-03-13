from django.forms import ModelForm
from django import forms
from .models import *

class OrderAddForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'
        exclude = ['status', 'start']



class OrderEditForm(ModelForm):
    class Meta:
        model = Deal
        fields='__all__'


class ContactAddForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'

class ContactEditForm(ModelForm):
    class Meta:
        model = Contact
        fields='__all__'
