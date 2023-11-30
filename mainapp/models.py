import os.path
import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_tag = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.category_tag}'


class Product(models.Model):
    product_name = models.CharField(max_length=40)
    product_code = models.CharField(max_length=20, unique=True)
    product_price = models.IntegerField()
    product_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to='images/', null=True, default='images/default.jpg')
    product_pdf = models.FileField(upload_to='pdf/', default='pdf/product.pdf', blank=True, null=True)
    sale = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_code} - {self.product_name}'


class CustomUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default-user.png', blank=True,
                                        null=True)

    def __str__(self):
        return f'{self.user.username}'


class TeamMember(models.Model):
    roles = (
        ("web_admin", "Web Admin"),
        ("content_manager", "Content Manager"),
        ("web_developer", "Web Developer"),
    )

    member_name = models.CharField(max_length=40)
    member_role = models.CharField(choices=roles, max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default-user.png', blank=True,
                                        null=True)

    def __str__(self):
        return f'{self.member_name} - {self.member_role}'
