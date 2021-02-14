from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from auth.models import Speciality, ProfileType


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(label="phone",
                                   widget=forms.TextInput(attrs={"placeholder": "+923**********"}))
    address = forms.CharField(widget=forms.Textarea())
    speciality = forms.ChoiceField(choices=[(
        speciality.id, speciality.speciality) for speciality in Speciality.objects.all()])
    profile_type = forms.ChoiceField(choices=[(
        profile_type.id, profile_type.profile_type) for profile_type in ProfileType.objects.all()])

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email",
                  "phone_number", "address", "speciality", "profile_type", "password1", "password2")
