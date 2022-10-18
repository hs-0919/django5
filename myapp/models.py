from django.db import models

# Create your models here.
# Database Table를 class로 선언하는 곳

class Article(models.Model):
    code = models.CharField(max_length = 10)
    name = models.CharField(max_length = 10)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    





