from django import forms
from website.models import Contact,NewsLetter

class ContactForm(forms.ModelForm):
  
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