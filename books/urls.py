from django.urls import path

from .views import BooksListView, BookDetailView,SearchResultListView

urlpatterns = [
    path("<uuid:pk>/", BookDetailView.as_view(), name= "book_detail"),
    path("", BooksListView.as_view(), name="book_list"),
    path("search/", SearchResultListView.as_view(), name="search_result"),

]