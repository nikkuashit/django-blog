from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def signUp(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('test')
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            # return redirect('sign-up')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def signIn(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('loggedin')
            print(user)
            return redirect('blog/')
        else:
            print(user)
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'accounts/signin.html', context)
