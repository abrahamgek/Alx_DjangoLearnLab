# relationship_app/urls.py
from django.urls import path
from .views import LoginView, LogoutView, LibraryDetailView, register
from .views import register
from .views import list_books
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(template_name = 'relationship_app/library_detail.html'), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]