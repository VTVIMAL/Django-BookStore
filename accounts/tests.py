from django.contrib.auth import get_user_model
from django.test import TestCase

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

