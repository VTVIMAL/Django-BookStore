from django.urls import path

from .views import BooksListView, BookDetailView

urlpatterns = [
    path("<uuid:pk>/", BookDetailView.as_view(), name= "book_detail"),
    path("", BooksListView.as_view(), name="book_list"),
]