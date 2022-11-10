from django.views.generic import ListView,DetailView
from django.shortcuts import render

from .models import Book
# Create your views here.

class BooksListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"