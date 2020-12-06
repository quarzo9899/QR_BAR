from django.db import models

class Menù(models.Model):
    ultima_modifica = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Menù"
        verbose_name_plural = "Menù"

class Sezione(models.Model):
    menù = models.ForeignKey(Menù, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"

class Alimento(models.Model):
    sezione = models.ForeignKey(Sezione, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    prezzo = models.FloatField()
    ingredienti = models.CharField(max_length=400)
    image_url = models.FileField()
    # altro come la gradazione alcolica, litri ecc.
    altro = models.TextField(blank=True, default='')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Alimento"
        verbose_name_plural = "Alimenti"

class Cliente(models.Model):
    menù = models.ManyToManyField(Menù, related_name='menù')
    nome = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=400)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"

