from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import EmailForm
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
# Create your views here.

class HomeView(View):
    def get(self,request):
        form = EmailForm()
        context = {
            'form':form
        }
        return render(request, 'CV/index.html',context)
    def post(self,request):
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                mess_mail = form.cleaned_data['message']+'\nEmail: '+form.cleaned_data['email']
                send_mail(subject = form.cleaned_data['subject'],message= mess_mail,from_email='duonganhtuanbkdn@gmail.com', recipient_list= ['duonganhtuan1314@gmail.com'])
            except BadHeaderError:
                messages.error(request, 'Cant not send email')
                return HttpResponseRedirect(self.request.path_info)
            messages.success(request, 'Send successful')
            return HttpResponseRedirect(self.request.path_info)
