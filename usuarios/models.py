from django.contrib.auth.models import User, Group
from django.db import models


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.grupo.name if self.grupo else 'Sem grupo'}"
