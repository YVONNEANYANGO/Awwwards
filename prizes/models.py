from django.db import models

# Create your models here.
class Profile(models.Model):
    profile = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length = 500)
    projects = models.ForeignKey(projects)
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

