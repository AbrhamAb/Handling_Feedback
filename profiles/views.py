from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView   

from .models import UserProfile
# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    fields = "__all__"

class ProfilesView( ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"