from django.forms import ModelForm
from django import forms
from .models import *

class CommentForm(ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class' : 'input', 'placeholder' :'Your name'
    }))
    
    body = forms.CharField(max_length=100,widget=forms.Textarea(attrs={
        'class' : 'input', 'placeholder' :'Comment Here', 'rows' : 3
    }))
    class Meta:
        model = MainComment
        fields = ['name','body']

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PostCommentForm(ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class' : 'input', 'placeholder' :'Your name'
    }))
    
    body = forms.CharField(max_length=100,widget=forms.Textarea(attrs={
        'class' : 'input', 'placeholder' :'Comment Here', 'rows' : 3
    }))
    class Meta:
        model = Comment
        fields = ['name','body']

class FeaturedCommentForm(ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={
        'class' : 'input', 'placeholder' :'Your name'
    }))
    
    body = forms.CharField(max_length=100,widget=forms.Textarea(attrs={
        'class' : 'input', 'placeholder' :'Comment Here', 'rows' : 3
    }))
    class Meta:
        model = FeaturedComment
        fields = ['name','body']