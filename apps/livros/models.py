from django.db import models

# Create your models here.

class Livros(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    tipo = models.IntegerField()

    def __str___(self):
        return f'Nome: {self.nome}: {self.autor}: {self.tipo}' #define a forma como aparece na APP


 