from django.db import models
from apps.usuario.models import Usuario

# Create your models here.

class SeccionBanner(models.Model):
	texto = models.CharField(max_length=150)
	background = models.FileField(upload_to='static/images')
	logo = models.FileField(upload_to='static/images')

class SeccionNoticias(models.Model):
	titulo = models.CharField(max_length=50)
	resumen = models.CharField(max_length=80)
	texto = models.CharField(max_length=200)
	image = models.FileField(upload_to='static/images')

class SeccionDeMedios(models.Model):
	logo = models.FileField(upload_to='static/medios') 
	texto = models.CharField(max_length=100)

class SeccionPatrocinantes(models.Model): 
	logo = models.FileField(upload_to='static/patrocinantes')

class SeccionClientes(models.Model):
	id_usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	historia = models.CharField(max_length=100)

class SeccionPortafolios(models.Model):
	logo = models.FileField(upload_to='static/portafolio') 
