from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




# Create your models here.
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)

class AccountManager(BaseUserManager) :
    def create_user(self, first_name, last_name, email, username, gender, dob, password=None) :
        if not first_name :
            raise ValueError("User must provide the first name")
        if not email :
            raise ValueError("User must provide an email")
        if not username :
            raise ValueError("User must provide a username")
        if not gender :
            raise ValueError("User must provide the gender")
        if not dob :
            raise ValueError("User must provide date of birth")
        
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
            gender = gender,
            dob = dob
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, first_name, last_name, email, username, gender, dob, password) :
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username= username,
            dob=dob,
            gender=gender,
            password=password
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()
        return user
        
        

class Account(AbstractBaseUser) :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dob', 'first_name', 'last_name', 'gender']
    
    def __str__(self) :
        return self.username
    
    def has_perm(self, perm, obj=None) :
        return self.is_admin
    
    def has_module_perms(self, app_label) :
        return True
    