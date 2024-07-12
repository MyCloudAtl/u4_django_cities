from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100, default='no name')
    category = models.CharField(max_length=100, default = 'no category')
    description = models.TextField(default= 'no default')
    image_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100, default = 'no reviewer')
    comment = models.TextField(default= 'no default')
    reviewer_company = models.CharField(max_length=100, default = 'no company')

    def __str__(self):
        return f"{self.reviewer_name} review for {self.attraction.name}"