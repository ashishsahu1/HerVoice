from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Relationship
# from .forms import ProfileModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def my_profile_view(request):
    pass
