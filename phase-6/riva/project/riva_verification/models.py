from django.db import models

class Product(models.Model):
    code = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
