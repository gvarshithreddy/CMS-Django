from django.shortcuts import render

# Create your views here.

def staffHome(request):
    return render(request, 'staffHome.html')