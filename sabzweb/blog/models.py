from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB','Published'
        REJECTED = 'RJ','Rejected'
    #relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    # data fields
    title = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=250)

    #date
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #choises fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['published'])
        ]

    def __str__(self):
        return self.title


