from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length = 500)
    projects = models.ForeignKey(User, on_delete=models.CASCADE)
    contacts = models.CharField(max_length = 20)


    # Methods
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()

    def __str__(self):
        return self.User

    @classmethod
    def get_profile(cls, profile_id):
        profile = Profile.objects.filter(name__username__icontains=profile_id)
        return profile

class Project(models.Model):
    User = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    landing_page = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 500)
    link = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add=True)

    # Methods
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def update_project():
        self.update()

    def __str__(self):
        return self.Project