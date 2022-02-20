import email
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AppUserManger(BaseUserManager):
    def create_user(self,phone_number,first_name,last_name,email,password = None):
        if not phone_number:
            return ValueError(' Please enter a valid phone number')
        if not first_name:
            return ValueError(' Please enter a your first_name')
        if not last_name:
            return ValueError(' Please enter your last_name')

        if not email:
            return ValueError(' Please enter a valid email')
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_supeuser(self,phone_number,email,first_name,last_name,password =None):
        user = self.create_user(
            email=self.normalize_email(email),
            phone_number=phone_number,
            first_name= first_name,
            last_name=last_name,
            password=password
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using = self._db)

        return user

        

# Create your models here.
class AppUser(AbstractBaseUser):
    first_name = models.CharField(verbose_name='enter first name', null=False, max_length=100)
    last_name = models.CharField(verbose_name='enter last name', null=False, max_length=100)
    email = models.EmailField(verbose_name='enter last name', null= False)
    phone_number =  models.CharField(verbose_name='enter valid phone number', null=False, max_length=20)
    cat= (
        ('Buyer','Buyer'),
        ('Seller','Seller'),
    )
    category = models.CharField(verbose_name='sing up as ', max_length=20)
    

    #fileds to sellers
    Shop_name = models.CharField(max_length=200, verbose_name= 'enter shop name')
    com = (
       ("Electronics","Electronics") ,
       ("Clothes","Clothes") ,
       ("Food","Food") ,
       ("House to let","House to let") ,
       ("Furniture","Furniture") ,
    )
    commodities = models.CharField(max_length=200, verbose_name="Shop category")
    location = models.CharField(max_length=200, verbose_name='Shops location')
    date_joined = models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name','email']

    objects =AppUserManger()


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    


