#!/usr/bin/env python
__author__ = "Jonathan Morse"
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)