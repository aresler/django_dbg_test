from django.shortcuts import render

# Create your views here.

def index(request):
    word = 'world'  # BREAKPOINT here to test debugger in views
    return render(request, 'index.html', {'word': word})