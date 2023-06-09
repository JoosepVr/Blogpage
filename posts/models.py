# Create your models here.
from django.db import models
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return self.title
