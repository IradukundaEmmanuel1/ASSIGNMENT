from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Using auto_now_add automatically saves the current date when created
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title