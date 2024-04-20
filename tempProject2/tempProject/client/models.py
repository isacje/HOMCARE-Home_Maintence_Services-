from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
import uuid
from django.utils.translation import gettext_lazy as _

class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('You must provide an email.'))
        if not username:
            raise ValueError(_('You must provide an username.'))
        if not password:
            raise ValueError(_('You must provide an password.'))
        email = self.normalize_email(email)
        user=self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(_('You must provide an email.'))
        # if not username:
        #     raise ValueError(_('You must provide an username.'))
        # if not password:
        #     raise ValueError(_('You must provide an password.'))
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_staff = True  # Set is_staff to True for superuser
        user.is_superuser = True
        user.is_admin=True
        user.save(using=self._db)
        return user
    
    
class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150, blank=True)
    phoneNo=models.CharField(max_length=20)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    userType=models.CharField(max_length=10,null=True)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    # def __init__(self,username,email,password,phoneNo) -> None:
    #     self.username=username
    #     self.email=email
    #     self.password=password
    #     self.phoneNo=phoneNo
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class ServiceProvider(NewUser):
    clientID=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    companyName=models.CharField(max_length=50)
    ownerName=models.CharField(max_length=30)
    officeAddress=models.CharField(max_length=50)
    gstNo=models.CharField(max_length=30,unique=True)
    pan=models.CharField(max_length=10,unique=True,default=None)
    panName=models.CharField(max_length=200,unique=True,default=None)
    #file = models.FileField(upload_to='C:\Users\Dell\Documents\temp\tempProject\files')
    
    # def __init__(self,username,email,password,phoneNo,companyName,ownerName,officeAddress,gstNo) -> None:
    #     super().__init__(self,username,email,password,phoneNo)
    #     self.clientID = uuid.uuid4()
    #     self.companyName = companyName
    #     self.ownerName = ownerName
    #     self.officeAddress = officeAddress
    #     self.gstNo = gstNo
        
        
class Client(NewUser):
    userID=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    address=models.CharField(max_length=50)
    # def __init__(self,username,email,password,phoneNo,address) -> None:
    #     super().__init__(self,username,email,password,phoneNo)
    #     self.userID = uuid.uuid4()
    #     self.address=address

class fileUpload(models.Model):
    fileID=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    ID=models.ForeignKey(ServiceProvider,to_field="clientID",on_delete=models.CASCADE)
    field_name = models.FileField(upload_to='C:/Users/Dell/Documents/temp/tempProject/media', max_length=254)
    

class Section(models.Model):
    # ID=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    sectionID=models.ForeignKey(ServiceProvider,to_field="clientID",on_delete=models.CASCADE,primary_key=True)
    title=models.CharField(max_length=50)    
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    employeeCount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=350)
    employeePerArea=models.DecimalField(max_digits=10,decimal_places=2)
    timeToComplete=models.DecimalField(max_digits=10,decimal_places=2)
    sectionType=models.CharField(max_length=20)
    
# class providerRegister():
#     serviceTitle=models.CharField(max_length=50)
#     rate=models.IntegerField(max_length=10)
#     description=models.CharField(max_length=350)
#     images = models.ImageField(upload_to='C:/Users/Dell/Documents/temp/tempProject/media', max_length=254)
#     employeeCount=models.IntegerField(max_length=10)

class serviceList(models.Model):
    ID=models.ForeignKey(ServiceProvider,to_field="clientID",on_delete=models.CASCADE,primary_key=True)
    title=models.CharField(max_length=50)
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    type=models.CharField(max_length=20)