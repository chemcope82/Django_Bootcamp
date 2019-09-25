from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import User
from AppTwo.forms import NewUserForm

def index(request):
    
    return render(request, 'app_two/index.html')
# Create your views here.
def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error, Form is Invalid')
    
    return render(request, 'app_two/users.html', {'form':form})