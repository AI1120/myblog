from django.db import models

# Create your models here.
Rating = [
    ('b', 'Bad'),
    ('a', 'Average'),
    ('e', 'Excellent')
]


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField()
    mfg_date = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(max_length=1, choices=Rating)

    def __str__(self):
        return self.name
    
    def show_desc(self):
        return self.description[:50]