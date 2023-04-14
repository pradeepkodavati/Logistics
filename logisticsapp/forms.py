from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User

from logisticsapp.models import routeLogistics


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class routeLogisticsForm(forms.ModelForm):
    class Meta:
        model = routeLogistics
        fields = ['vehicleNumber', 'route', 'status', 'destination', 'team']




class MyPasswordResetForm(PasswordResetForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))




