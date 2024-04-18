from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactForm,NewsLetterForm
from django.contrib import messages

def index_view(request):
  return render(request,'website/index.html')

def about_view(request):
  return render(request,'website/about.html')



def contact_view(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      success_message = "you'r ticket submited successfully"
      messages.add_message(request, messages.SUCCESS, success_message)
    else:
      error_message = "yout ricket didnt submited"
      messages.add_message(request, messages.ERROR, error_message)
  form = ContactForm()
  return render(request, 'website/contact.html', {'form': form})


def NewsLetter_view(request):
  if request.method =='POST':
    form=NewsLetterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
    else:
      messages.add_message(request,messages.ERROR,'your ticket didnt submited')
  form=NewsLetterForm()
  return render(request,'website/contact.html',{'form':form}) 