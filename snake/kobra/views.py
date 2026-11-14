from django.shortcuts import render

def game_view(request):
    return render(request, 'kobra/index.html')

# Create your views here.
