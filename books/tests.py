from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase,Client
from django.urls import reverse


from .models import Book, Review

# Create your tests here.

class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user( # setup for testing review
            username = "reviewuser",
            email = "reviewuser@email.com",
            password = "testing321",
        )
        cls.special_permission = Permission.objects.get(
            codename="special_status"
        ) 
        cls.book = Book.objects.create(
            title = "Harry Potter", 
            author = "JK Rowling", 
            price="25.00"
        )
        cls.review = Review.objects.create( # creating a review to test
            book = cls.book,
            author = cls.user,
            review = "an excellent review",
        )
    
    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")
    

    def test_book_listview_for_loggedin_users(self):
        self.client.login(email= "reviewuser@email.com", password = "testing321")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    
    def test_book_listview_for_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" % (reverse("account_login")))
        response = self.client.get("%s?next=/books/" % (reverse("account_login")))
        self.assertContains(response, "LogIn")


    def test_book_detail_view_with_permissions(self):
        self.client.login(email= "reviewuser@email.com", password = "testing321")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/1233/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "an excellent review") # testing if review exist
        self.assertTemplateUsed(response, "books/book_detail.html")


    # def test_book_listview(self):
    #     response = self.client.get(reverse("book_list"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Harry Potter")
    #     self.assertTemplateUsed(response, "books/book_list.html")
    
    # def test_book_detail_view(self):
    #     response = self.client.get(self.book.get_absolute_url())
    #     no_response = self.client.get("/books/1233/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, "Harry Potter")
    #     self.assertContains(response, "an excellent review") # testing if review exist
    #     self.assertTemplateUsed(response, "books/book_detail.html")
