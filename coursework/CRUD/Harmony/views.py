from django.shortcuts import render

# Create your views here.

def lyrics(request):
    return render(request, 'lyrics.html') 
