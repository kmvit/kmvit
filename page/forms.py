from django import forms
from .views import *
from .models import *

class FeedBackAdd(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'