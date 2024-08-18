# relationship_app/views.py
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import register
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import login
from django.contrib.auth.forms import logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

# Function-based view to list all books

# relationship_app/views.py

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


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def user_login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
        else:
            form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})