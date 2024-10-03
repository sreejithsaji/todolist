from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)

    status_option=(
        ("complete","complete"),
        ("incomplete","incomplete")
    )

    status=models.CharField(max_length=100,choices=status_option,default="incomplete")

    created_date=models.DateTimeField(auto_now_add=True)
