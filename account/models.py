from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError(
                'email АЯНТЧАСЫ ТОЛТУРУЛУУГА ТИЙИШ'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def  create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)
    
    def  create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)
    


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=100, verbose_name='ЭЛЕКТРОНДУК ДАРЕГИНИЗ', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='АТЫНЫЗ')
    last_name = models.CharField(max_length=70, verbose_name='ФАМИЛИЯНЫЗ')    
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    dateJoined = models.DateTimeField(auto_now_add=True)
    activation_code = models.CharField(max_length=50, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff
    
    def create_activation_code(self):
        code = get_random_string(10)
        self.activation_code = code
        self.save()