#!/usr/bin/env python
__author__ = "Jonathan Morse"
from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
