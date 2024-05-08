from django import forms
from website.models import Contact,NewsLetter
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
  captcha = CaptchaField()
  class Meta:
    model=Contact
    fields='__all__'
  # def clean(self):
  #   clean_data=super().clean()
  #   clean_data['name']='UNKNOWN'
  #   return clean_data
    
class NewsLetterForm(forms.ModelForm):
  class Meta:
    model=NewsLetter
    fields='__all__'
    
