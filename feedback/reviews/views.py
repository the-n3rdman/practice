from . import forms
from . import models
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.


def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST['user_name']
    #     # this is manually handling the form errors, hence django forms will help to automate this process
    #     if entered_username == '':
    #         return render(request, 'reviews/review.html', {'has_error': True})

    #     return HttpResponseRedirect('/thank_you')
    # return render(request, 'reviews/review.html', {'has_error': False})

    # using Form class from forms.py

    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = models.Review(user_name=form.cleaned_data['user_name'],
                                   review_text=form.cleaned_data['review_text'],
                                   rating=form.cleaned_data['rating'])
            return HttpResponseRedirect('/thank_you')
    else:
        # adding an else here so if the request method is get then only new form is shown but if get method is post and form is invalid then the form with errors is renderd
        form = forms.ReviewForm()
    return render(request, 'reviews/review.html', {'form': form})


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
