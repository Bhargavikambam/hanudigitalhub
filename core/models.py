from django.db import models

# 📩 Contact Form Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 🖼️ Portfolio Model
class Portfolio(models.Model):
    title = models.CharField(max_length=100, default='Portfolio Title')   
    project_image = models.ImageField(upload_to='portfolio/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


# ⚙️ Services Model
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title