from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Partnership(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    equity_percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.creator} - {self.business}'
