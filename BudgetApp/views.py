from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'Home.html')



def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'Form.html')
