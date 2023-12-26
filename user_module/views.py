from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'landing_page.html')

def index(request):
    return render(request,'dashboard-ecommerce.html')

def index1(request):
    return render(request,'dashboard-ecommerce1.html')