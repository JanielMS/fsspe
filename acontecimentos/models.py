from django.db import models


class Acontecimento(models.Model):
    titulo = models.CharField(max_length=150)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to="acontecimentos/", blank=True, null=True)

    def __str__(self):
        return self.titulo
    
    
    
