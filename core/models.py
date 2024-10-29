from django.db import models

class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200, blank=True)
    site_description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    
    def __str__(self):
        return self.site_title

class About(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # প্রোফাইল ছবি
    bio = models.TextField()  
    skills = models.TextField()  
    links = models.TextField(blank=True, null=True)  
    cv_file = models.FileField(upload_to='cv_files/', blank=True, null=True) 

    def save(self, *args, **kwargs):
        self.skills = self.skills.strip()  # Trim whitespace
        super().save(*args, **kwargs)

    def __str__(self):
        return "About Me"


class Contact(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    phone = models.CharField(max_length=15, blank=True, null=True)  
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')

    def __str__(self):
        return self.name
