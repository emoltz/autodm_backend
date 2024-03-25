from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_admin = models.BooleanField(_('superuser status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Character(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    dnd_class = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    # stats
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    # inventory
    inventory = models.JSONField(default=dict)

    @staticmethod
    def get_modifier(stat: int) -> int:
        return (stat - 10) // 2

    def get_all_modifiers(self) -> dict[str, int]:
        return {
            "strength": self.get_modifier(self.strength),
            "dexterity": self.get_modifier(self.dexterity),
            "constitution": self.get_modifier(self.constitution),
            "intelligence": self.get_modifier(self.intelligence),
            "wisdom": self.get_modifier(self.wisdom),
            "charisma": self.get_modifier(self.charisma)
        }



    def save(self, *args, **kwargs):
        if self.level < 1:
            self.level = 1
        super(Character, self).save(*args, **kwargs)