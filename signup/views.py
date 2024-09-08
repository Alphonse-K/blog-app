# from django.shortcuts import render
from django.views.generic.edit import CreateView
from signup.forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = 'signup/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)