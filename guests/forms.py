from django.forms import ModelForm

from guests.models import Signin


class SigninForm(ModelForm):

    class Meta:
        model = Signin
        fields = ['name']