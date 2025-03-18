from django.db import models


class Projeto(models.Model):
    # Status do projeto
    STATUS_PROJETO_CHOICES = [
        ("finalizado", "Finalizado"),
        ("em_andamento", "Em andamento"),
        ("nao_finalizado", "Não Finalizado"),
        ( "cancelado", "Cancelado")
    ]

    # Status de implantação
    STATUS_IMPLANTACAO_CHOICES = [
        ("nao_implantado", "Não Implantado"),
        ("implantado", "Implantado"),
    ]

    # Status do registro de software
    STATUS_REGISTRO_CHOICES = [
        ("nao_registrado", "Não Regristrado"),
        ("registro_andamento", "Registro em Andamento"),
        ("registro_concluido", "Registro Concluído"),
    ]

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nome_abreviado = models.CharField(max_length=8)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    equipe = models.TextField(blank=True, null=True)
    nome_da_equipe = models.CharField(max_length=100, blank=True, null=True)
    link_do_projeto = models.URLField(blank=True, null=True)
    cliente = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # Campos de status
    status_projeto = models.CharField(
        max_length=20,
        choices=STATUS_PROJETO_CHOICES,
        default="em_andamento"
    )
    
    status_implantacao = models.CharField(
        max_length=20,
        choices=STATUS_IMPLANTACAO_CHOICES,
        default="nao_implantado"
    )

    status_registro = models.CharField(
        max_length=20,
        choices=STATUS_REGISTRO_CHOICES,
        default="nao_registrado"
    )

    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.get_status_projeto_display()}"
    
