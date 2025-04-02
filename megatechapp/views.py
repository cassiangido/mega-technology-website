from django.shortcuts import render
# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def careers(request):
    return render(request, 'careers.html')


