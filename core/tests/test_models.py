from django.test import TestCase
from django.test.client import Client

from model_mommy import mommy
from Courses.models import Course


class CourseManagerTestCase(TestCase):

    def setUp(self):
        self.courses_django = mommy.make(
            'Course', name_course='Python na Web com Django', _quantity=10
        )

        self.courses_django = mommy.make(
            'Course', name_course='Python para devs', _quantity=10
        )

        # self.client = Client()

    
    def tearDown(self):
        Course.objects.all().delete()   

    
    def test_course_search(self):
        search = Course.objects.search('django')
        self.assertEqual(len(search), 10)

        search = Course.objects.search('devs')
        self.assertEqual(len(search), 10)
