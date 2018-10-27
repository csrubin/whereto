#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from barFinder.forms import UserInput

def index(request):
    return render(request, 'index.html',{})

def getInput(request):
    if request.method == 'POST':
        MyUserInput = UserInput(request.POST)

        if MyUserInput.is_valid():
            # Processing 

            return HttpResponseRedirect()
    else:
         MyUserInput = UserInput()

    return render(request, 'index.html',{'MyUserInput': MyUserInput})
