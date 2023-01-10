from django.db import models


class User(models.Model):
    id = models.AutoField('Primary Key', primary_key=True)
    username = models.CharField('Username', max_length=100)
    password = models.CharField('User Password', max_length=20)
    type = models.CharField('Type', max_length=15, default='normal')
