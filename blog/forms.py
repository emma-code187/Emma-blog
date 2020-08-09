from django import forms
from .models import Post, Comment
from django.shortcuts import render, redirect, get_object_or_404


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = [ 'name', 'email', 'body' ]