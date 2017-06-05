from django.db import models
from django.contrib.auth.models import User
from apps.tecnologia.models import SeccionClientes

# Create your models here.

class Usuario(User):
	id_usuario = models.AutoField(primary_key=True)
	cedula = models.CharField(max_length=15)
	fecha_nac = models.DateField()
	empresa = models.CharField(max_length=30)
	direccion = models.TextField()

class perfilUsuario(models.Model):
	cedula = models.OneToOneField(Usuario)
	avatar = models.FileField(upload_to='static/avatar')
	