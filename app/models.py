from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = "User"
    user_name = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=50, blank=False, null=True)
    specilist = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    ward = models.IntegerField()
    salt = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


class Role(models.Model):
    class Meta:
        db_table = "Role"

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class StaffRole(models.Model):
    class Meta:
        db_table="Staff Roles"
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    roles=models.ManyToManyField(Role)