from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import RegForm, AccountInfoForm


User = get_user_model()


def indexpage(request):
    return render(request, 'users/index.html')


def registration(request):
    title = 'Регистрация'
    success_message = ''
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            success_message = 'Вы успешно зарегистрировались! Войдите в аккаунт!'
            messages.success(request, success_message)
            return redirect('login')
    else:
        form = RegForm()
    return render(request, 'users/registration.html', {'form': form,
                                                       'title': title,
                                                       'success_message': success_message})


def profile(request):
    if request.method == 'POST':
        form = AccountInfoForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = AccountInfoForm()
    return render(request, 'users/profile.html', context={'form': form})
