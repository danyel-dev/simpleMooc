from django.test import TestCase
from django.test.client import Client


class HomeViewTest(TestCase):
    
    def test_home_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_home_template_used(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'base.html')
