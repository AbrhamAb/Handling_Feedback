from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     username = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),error_messages={'required': 'Please enter your name.'})
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea(attrs={'placeholder': 'Write your review here...'}), error_messages={'required': 'Please write a review.'})
#     rating = forms.IntegerField(label='Rating (1-5)', min_value=1, max_value=5, error_messages={'required': 'Please provide a rating between 1 and 5.', 'min_value': 'Rating must be at least 1.', 'max_value': 'Rating cannot be more than 5.'})

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = '__all__'

        labels = {
            'username': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Rating (1-5)',
        }

        error_messages= {
            'username': {
                'required': 'Please enter your name.',
            },
            'review_text': {
                'required': 'Please write a review.',
            },
            'rating': {
                'required': 'Please provide a rating between 1 and 5.',
                'min_value': 'Rating must be at least 1.',
                'max_value': 'Rating cannot be more than 5.',
            },
        }