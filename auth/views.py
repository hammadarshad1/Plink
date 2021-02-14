from django.shortcuts import render
from django.db import transaction
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

from auth import forms
from auth.models import Profile, Speciality, ProfileType


class RegisterView(FormView):

    template_name = "registration/register.html"
    form_class = forms.RegisterForm
    success_url = "/user/login/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse
        try:
            with transaction.atomic():
                form.save()
                breakpoint()
                Profile.objects.create(user=form.instance,
                                       address=form.cleaned_data["address"],
                                       phone_number=form.cleaned_data["phone_number"],
                                       speciality=Speciality.objects.get(
                                           id=form.cleaned_data["speciality"]),
                                       profile_type=ProfileType.objects.get(id=form.cleaned_data["profile_type"]))
                return super().form_valid(form)
        except Exception as e:
            print(e)
