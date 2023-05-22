from django.db import models
import datetime
import uuid

# Create your models here.

class User(models.Model):
    
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ("Others","Others"),
    )
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    mobile = models.IntegerField()
    password = models.CharField(max_length=20000)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=15,choices = GENDER)
    unique_id = models.UUIDField(default=uuid.uuid4,editable=False)

    def __str__(self):
        return self.name+" X "+str(self.unique_id)


class Post(models.Model):
    title = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    view = models.IntegerField(default=0)
    detail = models.TextField(max_length=100000)
    created_at = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(datetime.datetime.now())

    def __str__(self):
        return self.name
    
class subscription(models.Model):
    email = models.EmailField(max_length=100)
    ip = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    