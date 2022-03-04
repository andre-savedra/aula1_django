from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=55)
    idUser = models.BigIntegerField()
    email = models.CharField(max_length=80)
    fone = models.CharField(max_length=15, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
