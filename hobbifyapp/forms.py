from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Hobby

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "address", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        return user


class NewHobbyForm(ModelForm):
    class Meta:
        model = Hobby
        fields = ['hobby_name', 'description']
