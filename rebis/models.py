from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField(blank=True)
    votes = models.IntegerField(default=0)
    tips = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    queue = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)

    def is_money(self):
        if self.tips > 0:
            return True
        else:
            return False

    class Meta:
        ordering = ['-votes', '-tips',]
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
