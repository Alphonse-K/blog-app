from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.datetime.today)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)

    def __str__(self):
        return self.title