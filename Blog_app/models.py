from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='images123')
    category = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True, default=None, related_name='liked')

    def __str__(self):
        return self.title

    # property
    def num_likes(self):
        return self.liked.all().count()


class Comments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    commented_in = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='commented_in')


Like_choices = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(choices=Like_choices, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
