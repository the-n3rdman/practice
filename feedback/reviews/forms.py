from django import forms
from . import models

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=100, error_messages={
#         "required": "Name field cant be empty",
#         "max_length": "please enter a shorter name"
#     })
#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea)
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Review'
        }
        error_messages = {
            'user_name': {
                "required": "Name field cant be empty",
                "max_length": "please enter a shorter name"
            }
        }
