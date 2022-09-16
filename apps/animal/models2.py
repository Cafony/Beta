from operator import length_hint
from unittest.util import _MAX_LENGTH
from django import models


# Criar model
class Animal(models.Model):
    nome = models.CharField(_MAX_LENGTH
    