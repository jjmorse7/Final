#!/usr/bin/env python
__author__ = "Jonathan Morse"
from django.urls import path

from .views import HomePageView, TestPageView

urlpatterns = [
    path("test", TestPageView.as_view(), name="test"),
    path("", HomePageView.as_view(), name="home"),
]