from django.db import models
from datetime import *
from django.contrib.auth.models import User
# Create your models here.

estado_choices = [
    ("Busca","Busca"),
    ("Pendente","Pendente"),
    ("Por Digitalizar","Por Digitalizar"),
    ("Digitalizado","Digitalizado"),
    ("Assinatura","Assinatura"),
    ("Pronto a Levantar","Pronto a Levantar"),
    ("Concluido","Concluido"),
]

estado_peticao_choices = [
    ("Diferido","Diferido"),
    ("Sem Diferimento","Sem Diferimento"),
    ("Gabinete do Director","Gabinete do Director"),
]

observacao_choices = [
    ("Secretária", "Secretária"),
    ("Sistema", "Sistema"),
]

parentesco_choices = [
    ("Proprietário", "Proprietário"),
    ("Pai","Pai"),
    ("Mãe", "Mãe"),
    ("Irmão(ã)", "Irmão(ã)"),
    ("Tio(a)", "Tio(a)"),
    ("Amigo", "Amigo"),
    ("Outros", "Outros"),

]

class Certificado (models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    bi = models.CharField(max_length=14, verbose_name="Bilhete de Identidade")
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=datetime.now(), verbose_name="Data de Entrada")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Funcionário")
    observacao = models.CharField(max_length=50, choices=observacao_choices, verbose_name="Observação")
    nota = models.TextField(max_length=200, default="Nenhuma")
    estado = models.CharField(max_length=50, choices=estado_choices, default="Busca")

class Declaracao (models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    bi = models.CharField(max_length=14, verbose_name="Bilhete de Identidade")
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=datetime.now(), verbose_name="Data de Entrada")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.TextField(max_length=200, default="Nenhuma")
    estado = models.CharField(max_length=50, choices=estado_choices, default="Busca")

class Peticao (models.Model):
    numero_peticao = models.IntegerField(verbose_name="Número do Documento")
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=datetime.now(), verbose_name="Data de Entrada")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    assunto = models.CharField(max_length=100)
    nota = models.TextField(max_length=200, default="Nenhuma")
    estado = models.CharField(max_length=50, choices=estado_peticao_choices, default="Sem Diferimento")

class Historico (models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    bi = models.CharField(max_length=14, verbose_name="Bilhete de Identidade")
    quantidade = models.IntegerField()
    data = models.DateTimeField(default=datetime.now(),verbose_name="Data de Entrada")
    ano = models.CharField(max_length=50)
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.TextField(max_length=200, default="Nenhuma")
    estado = models.CharField(max_length=50, choices=estado_choices, default="Busca")

class Levantamento_Certificado(models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    data = models.DateTimeField(default=datetime.now(),verbose_name="Data de Levantamento")
    parentesco = models.CharField(max_length=50, choices = parentesco_choices,verbose_name="Grau de Parentesco")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.TextField(max_length=200, default="Nenhuma")
    documento = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.nome_utente}-{self.documento}-{self.data}"
    
class Levantamento_Declaracao(models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    data = models.DateTimeField(default=datetime.now(),verbose_name="Data de Levantamento")
    parentesco = models.CharField(max_length=50, choices = parentesco_choices,verbose_name="Grau de Parentesco")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.TextField(max_length=200, default="Nenhuma")
    documento = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.nome_utente}-{self.documento}-{self.data}"
    
class Levantamento_Historico(models.Model):
    nome_utente = models.CharField(max_length=200, verbose_name="Nome do Utente")
    data = models.DateTimeField(default=datetime.now(),verbose_name="Data de Levantamento")
    parentesco = models.CharField(max_length=50, choices = parentesco_choices,verbose_name="Grau de Parentesco")
    funcionario = models.ForeignKey(User, on_delete=models.PROTECT)
    nota = models.TextField(max_length=200, default="Nenhuma")
    documento = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"{self.nome_utente}-{self.documento}-{self.data}"