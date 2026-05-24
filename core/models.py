from django.db import models 
from django.utils.text import slugify


# 📩 Contact Form Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


# 🖼️ Portfolio Model
class Portfolio(models.Model):
    title = models.CharField(max_length=100, default='Portfolio Title') 
    slug = models.SlugField(unique=True, blank=True)
    project_image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# ⚙️ Services Model
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)