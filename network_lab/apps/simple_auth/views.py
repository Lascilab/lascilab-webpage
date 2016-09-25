from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
class SimpleLogin(FormView):
    template_name = "simple_auth/login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(SimpleLogin, self).form_valid(form=form)

class SimpleLogout(RedirectView):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        print "Login out"
        return super(SimpleLogout, self).get(request, *args, **kwargs)
        