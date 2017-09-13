from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView

from guests.forms import SigninForm
from guests.models import Signin


class SigninListView(ListView):
    template_name = 'adv/signin_list.html'
    context_object_name = 'signins'
    queryset = Signin.objects.order_by('-created')


class SigninCreateView(CreateView):
    template_name = 'adv/signin_create.html'
    form_class = SigninForm
    success_url = '/'

