from django.db import models

class Product(models.Model):
    imagem = models.URLField(max_length=1000)
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    parcelamento = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(max_length=2500)
    preco_sem_desconto = models.FloatField(null=True, blank=True)
    percentual_desconto = models.FloatField(null=True, blank=True)
    tipo_entrega = models.CharField(max_length=10, choices=[('Full', 'Full'), ('Normal', 'Normal')])
    frete_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.nome