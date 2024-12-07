from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

@login_required
def redirect_after_login(request):
    if request.user.role == 'tenant':  # Rol inquilino
        return redirect('home')  # URL para crear citas
    elif request.user.role == 'admin':  # Rol administrador
        return redirect('home')  # URL para gestionar citas
    return redirect('home')  # En caso de un rol desconocido

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect_after_login(request)  # Redirige según el rol
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
