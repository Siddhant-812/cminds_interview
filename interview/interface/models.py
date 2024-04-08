from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, username, panel_num, member_num,password=None):
        if not username:
            raise ValueError("Username Required.")
        
        user = self.model(username=username, panel_num=panel_num, member_num=member_num)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, panel_num, member_num,password=None):

        user = self.create_user(username,password=password,panel_num=panel_num,member_num=member_num)
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):

    username = models.CharField(max_length=100,unique=True)
    panel_num = models.IntegerField()
    member_num = models.IntegerField()
    is_active = models.BooleanField(default=True)  
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["panel_num","member_num"]

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


