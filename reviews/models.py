from django.db import models
from django.utils.html import mark_safe

class Review(models.Model):
    author = models.CharField(max_length=100)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} on {self.date_posted.strftime('%Y-%m-%d')}"

    def stars(self):
        # Generates HTML for star ratings
        stars_html = mark_safe(''.join(['<i class="fas fa-star text-warning"></i> ' for _ in range(self.rating)]) +
                               ''.join(['<i class="far fa-star text-warning"></i> ' for _ in range(5 - self.rating)]))
        return stars_html
