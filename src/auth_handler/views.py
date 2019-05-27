from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import UserProfile
import re


def register_user(request):

    template_name = 'auth_handler/register.html'

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        org = request.POST.get('org')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(
                request, f'The passwords entered did not match.'
            )
            return render(request, template_name)

        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(
                request, f'That is not a valid email address.'
            )
            return render(request, template_name)

        elif ' ' not in name:
            messages.error(
                request, f'Please enter your FULL name.'
            )
            return render(request, template_name)

        else:
            try:
                user = UserProfile()
                user.name = name
                user.email = email
                user.org = org
                user.set_password(pass1)

                user.save()
            except IntegrityError:
                messages.error(
                    request, (f'This account already exists, login!')
                )
                return redirect('/login')

            auth = authenticate(email=email, password=pass1)
            login(request, auth)

            messages.success(
                request, (f'Account created successfully, '
                          'you are now logged in!')
            )
            return redirect('/')

    else:
        return render(request, template_name)


def login_user(request):

    template_name = 'auth_handler/login.html'

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            messages.error(
                request, f'This user does not exist.'
            )
            return render(request, template_name)

        if not user.check_password(password):
            messages.error(
                request, f'Username or password is incorrect.'
            )
            return render(request, template_name)

        login(request, user)

        messages.success(
            request, f'Login Successful!'
        )
        return redirect('/')

    else:
        return render(request, template_name)


def logout_user(request):
    logout(request)
    messages.success(
        request, f'Logged out successfully!'
    )
    return redirect('/')
