# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Book
from .forms import BookForm
from .forms import BookSearchForm
from django.shortcuts import render

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')



class BookListView(ListView):
    model = Book
    #template_name = 'list_books.html'
    template_name = 'pagination_books.html'
    context_object_name = 'books'
    paginate_by = 2


def search_book(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            object_list = Book.objects.filter(title__icontains=book_name)
            return render(request, 'list_books.html', {'form': form, 'object_list': object_list})
    else:
        form = BookSearchForm()
        object_list = Book.objects.all()

    return render(request, 'list_books.html', {'form': form, 'object_list': object_list})