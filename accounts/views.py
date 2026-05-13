from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group  # Importação necessária para os grupos

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portfolio:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('portfolio:home')

def registo_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            
            try:
                grupo = Group.objects.get(name='autores')
                user.groups.add(grupo)
            except Group.DoesNotExist:
                pass
                
            login(request, user) 
            return redirect('portfolio:home')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/registo.html', {'form': form})