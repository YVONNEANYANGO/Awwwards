from django.test import TestCase
from .models import Profile,Project

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.cate= Profile(profile_pic = 'instarprofile.jpeg', bio = 'testing profile', projects = 'test projects posted', contacts = 'test contacts')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cate,Profile))
