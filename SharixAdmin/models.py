from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class SharixUser(AbstractUser):
    """
    Пользователь - здесь находиться описание сущности!
    """
    #pk = models.BigAutoField(help_text="А здесь можно добавить описание поля")
    phone_number = models.CharField(max_length=20, unique=True, blank=False, verbose_name='Номер телефона', help_text="А здесь можно добавить описание поля")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    @property
    def full_name(self):
        if self.first_name == "" or self.last_login  == "":
            return self.username
        else:
            return f"{self.first_name} {self.last_name}"
        
    class Meta:
        db_table = "auth_user"

# Create your models here.
