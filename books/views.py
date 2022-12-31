from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Book
# Create your views here.

class BooksListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "books/book_list.html"
    login_url = "account_login" # redirect to login page if user not logged in


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin , DetailView):
    '''If the user is logged in and is an author he is granted permission to view all books using the PermissionRequiredMixin'''
    model = Book
    template_name = "books/book_detail.html"
    login_url = "account_login" # redirect to login page if user not logged in
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related("reviews__author",)

class SearchResultListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_result.html"
    # queryset= Book.objects.filter(title__icontains="beginners")

    def get_queryset(self):
        query = self.request.GET.get("q") # q is the name of the form in base.html
        return Book.objects.filter( Q(title__icontains=query)| Q(title__icontains=query))