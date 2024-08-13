# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'published_date': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Select publication date', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ISBN number'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter summary', 'rows': 4}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }

class BookSearchForm(forms.Form):
    book_name = forms.CharField(
        label='Book name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hledání knihy'})
    )


