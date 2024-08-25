# relationship_app/urls.py
from django.urls import path
from .views import LoginView, LogoutView, LibraryDetailView, register
from .views import register
from .views import list_books
from .views import admin_view, librarian_view, member_view
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(template_name = 'relationship_app/library_detail.html'), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]