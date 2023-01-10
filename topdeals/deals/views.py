from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from topdeals.settings import BASE_DIR

from .forms import UserForm
from .models import User

# Create your views here.


def login(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            count = User.objects.filter(
                username=username, password=password).count()
            print(count)
            if count == 0:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html',{'form': form})
            else:
                # request.session['is_logged'] = True
                return redirect('home')
        else:
            return render(request, "login.html", {'form': form})

    return render(request, 'login.html', {'form': form})

def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            count = User.objects.filter(
                username=username, password=password).count()
            print(count)
            if count == 0:
                form.save()
                return redirect('login')
            else:
                # request.session['is_logged'] = True
                return redirect('home')
        else:
            return render(request, "login.html", {'form': form})

    return render(request, 'login.html', {'form': form})

# @login_required(login_url='')
def addDeals(request):
    return render(request, 'add-deals.html')