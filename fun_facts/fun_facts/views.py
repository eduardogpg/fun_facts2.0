from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader

from django.contrib.auth.models import User

from django.views.generic import CreateView

from django.core.urlresolvers import reverse_lazy

from .forms import CreateUserForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render(None, request))

def sign_in(request):
  template = loader.get_template('users/sign_in.html')
  return HttpResponse(template.render(None, request))

class SignUp(CreateView):
  success_url =  reverse_lazy('home')
  template_name = 'users/sign_up.html'
  model = User
  form_class = CreateUserForm

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.set_password ( self.object.password)
    self.object.save()
    return HttpResponseRedirect(self.get_success_url()) 

def logout(request):
  pass