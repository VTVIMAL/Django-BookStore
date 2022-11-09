from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse,resolve

# from .forms import CustomUserCreationForm
# from .views import SignUpView
# Create your tests here.

class CustomUserTest(TestCase):
    ''' if we are using the default User model we do not need for this test, but we are using the CustomUser model so we need to test it'''
    def test_create_user(self): # test for creating a normal user
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username = "testuser", email = "testuser@email.com", password= "testing321",
        ) 
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self): # test for creating a superuser
         
        user_model = get_user_model()
        admin_user = user_model.objects.create_superuser(
            username = "superuser", email = "superuser@email.com", password = "testing321",
        )
        self.assertEqual(admin_user.username, "superuser")
        self.assertEqual(admin_user.email, "superuser@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpTest(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I should be absent")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
    
