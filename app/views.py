from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required(login_url='/log_in/')
def user_list(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'example/user_list.html', {'users': users})


def log_in(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('user_list')
        else:
            print(form.errors)

    return render(request, 'example/log_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('log_in'))
        else:
            print(form.errors)

    return render(request, 'example/sign_up.html', {'form': form})


@login_required(login_url='/log_in/')
def log_out(request):
    logout(request)
    return redirect(reverse_lazy('log_in'))
