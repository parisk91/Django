from django.db import models

class Journalist(models.Model):
    firstname = models.CharField(max_length=30)
    lastname=models.CharField(max_length=40)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Article(models.Model):
    #author = models.CharField(max_length=50)
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=50)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"