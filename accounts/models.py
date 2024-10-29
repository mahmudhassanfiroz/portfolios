# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
import uuid
from django.utils.text import slugify

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email address must be provided"))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Username"), max_length=150, unique=True, blank=True, null=True)
    name = models.CharField(_("Full Name"), max_length=255)
    email = models.EmailField(_("Email Address"), unique=True, max_length=255)
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Mobile number must be in this format: '+999999999'. Up to 15 digits allowed.")
    )
    mobile = models.CharField(_("Mobile Number"), validators=[mobile_regex], max_length=17, blank=True, null=True, unique=True)
    profile_image = models.ImageField(_("Profile Image"), upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(_("Biography"), blank=True)
    
    is_staff = models.BooleanField(_("Staff Status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    is_email_verified = models.BooleanField(_("Email Verified"), default=False)
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)
    last_login = models.DateTimeField(_("Last Login"), blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ['-date_joined']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0] if self.name else self.email.split('@')[0]

    def save(self, *args, **kwargs):
        if not self.username:
            base_username = slugify(self.name) if self.name else self.email.split('@')[0]
            username = base_username
            while CustomUser.objects.filter(username=username).exists():
                username = f"{base_username}_{uuid.uuid4().hex[:8]}"
            self.username = username
        super().save(*args, **kwargs)

    # New fields added
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
