from __future__ import unicode_literals

from django.db import models

# Create your models here.


class type(models.Model):

  id = models.AutoField(primary_key=True)
  type = models.CharField(max_length=200, null=False, unique=True)


class product(models.Model):

  id = models.AutoField(primary_key=True)
  product = models.CharField(max_length=200, null=False, unique=True)
  price = models.IntegerField(null=False)
  ordered_number = models.IntegerField(null=False, default=0)
  link_image = models.CharField(max_length=200, null=False,default="Miss link")

  # Add foreign key
  type_id = models.ForeignKey('type')


class order(models.Model):

  id = models.AutoField(primary_key=True)
  ordered_number = models.IntegerField(default=0)
  ordered_time = models.DateTimeField(auto_now_add=True)

  # Add foreign key
  user_id  = models.ForeignKey('user')
  product_id = models.ForeignKey('product')


class user(models.Model):

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200, null=False,unique=True)
  phone = models.IntegerField(null=False, unique=True)

  # Add foreign key 
  order_id = models.ForeignKey('order')
