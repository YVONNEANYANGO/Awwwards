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

    # Testing Save Method
    def test_save_method(self):
        self.cate.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(editors) > 0)

    # Creating a new project and saving it
    self.new_project= Project(User = 'cate',title = 'Test Project',landing_page = 'image.jpeg',description = 'Random Project Test',link ='github', pub_date = 'Set time test')
    self.new_project.save()

def tearDown(self):
    Profile.objects.all().delete()
    Project.objects.all().delete()