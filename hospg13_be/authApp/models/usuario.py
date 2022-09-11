from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
            Crear y gardar un usuario con ursermane y password.
        """
        if not username:
            raise ValueError('Cada usuario debe tener un username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True,max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    perfil=models.CharField('Password', max_length = 30)
    nombre = models.CharField('Nombre', max_length = 35)
    apellidos = models.CharField('Apellidos', max_length = 35)
    telefono = models.CharField('Telefono', max_length = 35)
    genero = models.CharField('Genero', max_length = 35)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
