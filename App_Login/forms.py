from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(label="",required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'})
    )
    class Meta:
        model = User
        fields = ("username","email" ,"password1", "password2")


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}),required=False)
    class Meta:
        model = UserProfile
        exclude=('user',)
