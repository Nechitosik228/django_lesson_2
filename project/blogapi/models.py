from django.db import models

# Create your models here.

class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = "AD", "Admin"
        MEMBER = "MM", "Member"
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(choices=Role, max_length=2, default=Role.MEMBER)

    def __str__(self):
        return self.username

class Post(models.Model):
    class Progress(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.CharField(choices=Progress, max_length=2, default=Progress.DRAFT)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at'])
        ]
    
    def __str__(self):
        return self.title
