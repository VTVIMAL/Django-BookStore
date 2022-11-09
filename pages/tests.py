from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView,AboutPageView

# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        # response = self.client.get("/") # no longer needed because of setup
        return self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # response = self.client.get(reverse("home"))
        return self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        # response = self.client.get("/")
        return self.assertTemplateUsed(self.response, "home.html")
    
    def test_template_contains_correct_html(self):
        # response = self.client.get("/")
        return self.assertContains(self.response, "Home Page")
    
    def test_template_do_not_contain_incorrect_html(self):
        # response = self.client.get("/")
        return self.assertNotContains(self.response, "I should not be in the tempate") 

    def test_homepage_url_resolves_homepageview(self): # test that the homepage url resolves the homepage view
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")
    
    def test_aboutpage_does_not_contain_html(self):
        self.assertNotContains(self.response, "I should not exist")
    
    def test_aboutpage_resolve_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__ )