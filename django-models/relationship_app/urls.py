# relationship_app/urls.py
from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import views_register
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views_register, name='register'),
]