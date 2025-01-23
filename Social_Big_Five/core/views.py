from django.shortcuts import render

# Create your views here.

def take_test(request):
    return render(request, 'take-test.html')

def view_results(request):
    return render(request, 'view-results.html')