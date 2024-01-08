from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome = models.CharField(max_length=50, null=True)
    bi = models.CharField(max_length=14, null=True)
    contato1 = models.IntegerField(max_length=9, null=True)
    contato2 = models.IntegerField(max_length=9, null=True)
    imagem = models.ImageField(upload_to = "img/", default = "\img\img.jpg")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.usuario, self.nome)
