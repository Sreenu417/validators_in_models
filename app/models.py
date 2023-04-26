from django.db import models
from django.core import validators

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(11)])

    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,validators=[validators.MaxLengthValidator(10)])
    url=models.URLField(validators=[validators.MinLengthValidator(5)])
    email=models.EmailField()

    def __str__(self):
        return self.name
    
class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
