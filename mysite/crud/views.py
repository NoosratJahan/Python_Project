# Create your views here.

from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def home(request): 

    dictionary = {
        'title' : 'Application Form'
    }

    return render(request, 'crud/base.html', dictionary)

def form(request):
    user = User.objects.all()
    form = UserForm()
    context = {'user': user, 'form': form}

    if request.method == "POST":
        user = User.objects.all()
        form = UserForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect("/show")  
       
    return render(request, 'crud/form.html', context)
    
def update(request, id):
    user = User.objects.get(id=id)
    form=UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("/show")
        
    return render(request, 'crud/form.html', {'form': form})
            

def show(request):
    users = User.objects.all()
    return render(request, "crud/list.html", {'users': users})

def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("/show")


