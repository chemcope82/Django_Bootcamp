from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

def index(request):
    
    return(HttpResponse('<em>Go to /users to view a list of user data</em>'))
# Create your views here.
def users(request):
    users_dict = {'users':User.objects.order_by('last_name')}

    return(render(request,'app_two/users.html', context=users_dict))