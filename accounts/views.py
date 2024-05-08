from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout ,views as auth_views
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm , PasswordResetForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm , LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import  get_user_model
from django.contrib.auth.views import (PasswordChangeView,PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import reverse_lazy
from .forms import *

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.add_message(request,messages.SUCCESS,'Login was successful')
                return redirect('/')
            else:
                 messages.add_message(request,messages.ERROR,'The desired person was not found')
        return render(request, "registrations/login.html")
    else:
          return redirect('/')

# def login_view(request):
#   if not request.user.is_authenticated:
#     if request.method =='POST':
#       form= LoginForm(request=request,data=request.POST)
#       if form.is_valid():
#         username=form.cleaned_data.get('username',None)
#         email=form.cleaned_data.get('email',None)
#         password=form.cleaned_data.get('password')
#         user=None
#         if email:
#           user=authenticate(request,email=email,password=password)
#         elif username:
#           user=authenticate(request,username=username,password=password)
#         if user is not None:
#           login(request,user)
#           return redirect('/')
  
#   form=LoginForm()
#   context={'form':form}
#   return render(request,'account/login.html',context)

# def logout_view(request):
#   if request.user.is_authenticated:
#     logout(request)
#   return redirect('/')

@login_required
def logout_view(request):
  logout(request)
  return redirect('/')

def signup_view(request):
  if request.method=='POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      user= form.save()
      login(request,user)
      return redirect('/')
  else:
    form= RegistrationForm()
  
  context={'form': form}
  return render(request,'registrations/sign_up.html',context)

# def signup_view(request):
#   if not request.user.is_authenticated:
#     if request.method=='POST':
#       form=RegistrationForm(request.POST)
#       if form.is_valid():
#         form.save()
#         return redirect('/')
#     # form=UserCreationForm()
#     form=RegistrationForm()
#     context={'form':form}
#     return render(request,'account/sign_up.html',context)
#   else:
#     return redirect('/')
  

# Customized password change and reset views

# class ChangePasswordView(PasswordChangeView):
#     template_name = 'accounts/change_password.html'
#     success_url = reverse_lazy('account:user-setting')
#     form_class = ChangePasswordForm

class PasswordReset(PasswordResetView):
    template_name="registrations/password_reset_form.html"
    success_url=reverse_lazy("accounts:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="registrations/password_reset_done.html"
    success_url=reverse_lazy("accounts:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="registrations/password_reset_confirm.html"
    success_url=reverse_lazy("accounts:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="account/password_reset_complete.html"