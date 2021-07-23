from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['firstname']) < 3:
            errors['firstname_len'] = "nombre debe tener al menos 3 caracteres de largo";

        if len(postData['lastname']) < 2:
            errors['lastname_len'] = "apellido debe tener al menos 2 caracteres de largo";

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"


        if not SOLO_LETRAS.match(postData['firstname']) or not SOLO_LETRAS.match(postData['lastname']):
            errors['solo_letras'] = "solo letras en nombre y apellido porfavor"

        if len(postData['password']) < 8:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        return errors

class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=70)
    rol = models.CharField(max_length=30, default='COLABORADOR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    def __repr__(self):
        return f"{self.firstname} {self.lastname}" 


class BookManager(models.Manager):
    def validator(self, postData):
        errors={}
        if len(postData['title']) < 2:
            errors['title']="El titulo debe tener por lo menos 2 caracteres"
        if len(Book.objects.filter(title=postData['title'])) > 0:
            errors['title2']= "El libro ingresao ya existe en el sistema"
        if len(postData['description']) < 5:
            errors['description']="La descripción tiene que tener al menos 5 caracteres"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='books', null=True, on_delete=models.SET_NULL)
    users_who_like = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= BookManager()

    def __str__(self):
        return f"{self.id} {self.title} {self.description}>"

    def __repr__(self):
        return f" {self.id} {self.title} {self.description}>"