from django.shortcuts import render

# Create your views here.


def tribute(request):
    return render(request,'tribute.html')