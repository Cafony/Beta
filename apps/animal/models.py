from django.db import models

# Create your models here.


# Criar model
class Animal(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    idade = models.IntegerField()

    def __str___(self):
        return f'Nome: {self.especie}: {self.nome}'
    