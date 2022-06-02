from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def review(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        # this is manually handling the form errors, hence django forms will help to automate this process
        if entered_username == '':
            return render(request, 'reviews/review.html', {'has_error': TRUE})

        return HttpResponseRedirect('/thank_you')
    return render(request, 'reviews/review.html', {'has_error': False})


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
