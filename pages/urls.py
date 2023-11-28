#!/usr/bin/env python
__author__ = "Jonathan Morse"
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]