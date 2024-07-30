# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.BookCreateView.as_view(), name='add_book'),
    path('list/', views.BookListView.as_view(), name='list_book'),
    path('search/', views.search_book, name='search_book'),
]
