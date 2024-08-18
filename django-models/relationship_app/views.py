# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Define custom login view if needed
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Define custom logout view if needed
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Define custom registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})