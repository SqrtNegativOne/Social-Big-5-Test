from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TestForm

with open('questions.md', 'r') as file:
    questions = file.readlines()
    print(questions)

    
def take_test(request, user_id):
    if request.method == 'POST':
        form = TestForm(request.POST)

        # Server side validation
        if not form.is_valid:
            render(request, 'take-test.html', {
                'name': user_id,
                'form': form
            })
        
        # TODO: Add form results to database.
        print(form)

        return HttpResponseRedirect('core:view-results') # Fetches the url from urls.py


    return render(request, 'take-test.html', {
        'name': user_id,
        'form': TestForm()
    })

def view_results(request):
    return render(request, 'view-results.html')