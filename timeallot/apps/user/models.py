from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.core.mail import send_mail


class TimerUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            last_login=timezone.now()
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class TimerUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='email address')
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)

    is_active = models.BooleanField(
        default=True,
        help_text=('Designates whether this user should be treated as active.'
                   'Unselect this instead of deleting accounts.')
    )

    is_admin = models.BooleanField(default=False)

    objects = TimerUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        # All admins are staff
        return self.is_admin

    def get_full_name(self):
        return self.email.split("@")[0]

    def get_short_name(self):
        return self.email.split("@")[0]

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
