from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    fullName = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    phoneNumber = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ("fullName", "email", "phoneNumber", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
