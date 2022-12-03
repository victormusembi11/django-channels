from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


def user_list(request):
    return render(request, 'example/user_list.html')


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


def log_out(request):
    logout(request)
    return redirect(reverse_lazy('log_in'))
