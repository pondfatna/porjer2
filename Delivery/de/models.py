from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    autname = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0, null=True)
    live = models.CharField(max_length=200, null=True)

    # เพิ่ม related_name ที่นี่
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

    def __str__(self):
        return f'ชื่อ {self.autname} เพศ {self.sex} email {self.email} อายุ {self.age} ที่อยู่ {self.live}'
