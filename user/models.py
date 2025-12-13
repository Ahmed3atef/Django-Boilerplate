from django.db import models
from django.db.models import Q
from django_countries.fields import CountryField
from django.conf import settings


# using custom user model 
User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
    def by_username(self, username):
        return self.get(user__username=username)
    
    def by_name(self, first_name, last_name):
        return self.get(
            user__first_name=first_name,
            user__last_name=last_name
        )
    def search_by_name(self,query):
        return self.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        )

class Profile(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.OneToOneField('ProfileImage', on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    BOD = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    github_url = models.URLField(null=True, blank=True)
    insta_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    
    objects = ProfileManager()
    
class ProfileImage(models.Model):
    image = models.ImageField(upload_to='user/images')
    date_uploaded = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = CountryField()
    
    class Meta:
        indexes = [
            models.Index(fields=['country','state','city'])
        ]
