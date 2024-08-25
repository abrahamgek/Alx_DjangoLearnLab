# relationship_app/urls.py
from django.urls import path
from .views import LoginView, LogoutView, LibraryDetailView
from .views import user_register
from .views import list_books
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(template_name = 'relationship_app/library_detail.html'), name='library_detail'),
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
    path('register/', user_register, name='register'),
]