from django.contrib.auth.models import Group, Permission
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # การสร้าง user ทั่วไป
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # สร้าง superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    



class CustomUser(AbstractUser):
    autname = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0, null=True)
    live = models.CharField(max_length=200, null=True)

    # เพิ่ม related_name ที่นี่
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')
    objects = CustomUserManager()

    def __str__(self):
        return f'ชื่อ {self.autname} เพศ {self.sex} email {self.email} อายุ {self.age} ที่อยู่ {self.live}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
