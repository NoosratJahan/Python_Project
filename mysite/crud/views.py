# Create your views here.

from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def home(request): 

    dictionary = {
        'title' : 'Application Form'
    }

    return render(request, 'crud/base.html', dictionary)

def form(request, id=0):
    if request.method == "POST":

        if id==0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)

        if form.is_valid():                     
            form.save()
        return redirect("/show")
           
    else:
        if id == 0:
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'crud/form.html', {'form': form}) 
            

def show(request):
    users = User.objects.all()
    return render(request, "crud/list.html", {'users': users})

def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("/show")

