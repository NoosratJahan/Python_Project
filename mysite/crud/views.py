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

    if request.method == "POST":
        user = User()
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        user.FullName = name
        user.Email = email
        user.Phone = phone
        user.Address = address
        user.save()
        return redirect("/show")
    else:
        user = User()
        return render(request, 'crud/form.html', {'user': user})) 
    
def update(request, id):

    if request.method == "POST":
        user = User()
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        user.FullName = name
        user.Email = email
        user.Phone = phone
        user.Address = address

        user = User.objects.get(id=id)
        user=UserForm(request.POST,instance=user)
        user.save()
        user = User.objects.all()
        return redirect("/show")
    else:
        user = User()
        return render(request, 'crud/form.html', {'user': user})
            

def show(request):
    users = User.objects.all()
    return render(request, "crud/list.html", {'users': users})

def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("/show")

