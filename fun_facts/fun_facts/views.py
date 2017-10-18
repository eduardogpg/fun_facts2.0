from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import redirect

from django.template import loader

from django.contrib import messages
from django.contrib.auth.models import User

from django.views.generic import View
from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash

from .forms import CreateUserForm
from .forms import LoginForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render(None, request))

class SignIn(View):
  form = LoginForm()
  template = 'users/sign_in.html'

  def get(self, request, *args, **kwargs):
    return render(request, self.template, self.get_context())

  def post(self, request, *args, **kwargs):
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.add_message(request, messages.WARNING, 'Usuario o password invalidos')
    return render(request, self.template, self.get_context())

  def get_context(self):
    return {'form': self.form}

class SignUp(CreateView):
  success_url =  reverse_lazy('home')
  template_name = 'users/sign_up.html'
  model = User
  form_class = CreateUserForm

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.set_password (self.object.password)
    self.object.save()
    return HttpResponseRedirect(self.get_success_url()) 

def logout(request):
  pass