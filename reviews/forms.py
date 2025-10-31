from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),error_messages={'required': 'Please enter your name.'})
