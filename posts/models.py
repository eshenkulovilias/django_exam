from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts', default=None)
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'id': self.id})
