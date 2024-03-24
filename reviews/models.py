from django.db import models

class Review(models.Model):
    author = models.CharField(max_length=100)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} on {self.date_posted.strftime('%Y-%m-%d')}"
