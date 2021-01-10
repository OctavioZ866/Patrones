from django.db import models

# Create your models here.

class Tejidos(models.Model):
    partes = models.IntegerField()
    temperatura = models.FloatField()
    color = models.FloatField()
    inflamacion = models.FloatField()
    
    def __str__(self):
        return '( '+str(self.partes)+', '+str(self.temperatura)+', '+str(self.color)+', '+str(self.inflamacion)+' )'

class Grafo(models.Model):
    origen = models.ForeignKey(Tejidos, on_delete=models.CASCADE, related_name='origen')
    destino = models.ForeignKey(Tejidos, on_delete=models.CASCADE, related_name='destino')
    conectado = models.BooleanField()

    def __str__(self):
        registro1 =str(self.origen.partes)+', '+str(self.origen.temperatura)+', '+str(self.origen.color)+', '+str(self.origen.inflamacion)
        registro2 =str(self.destino.partes)+', '+str(self.destino.temperatura)+', '+str(self.destino.color)+', '+str(self.destino.inflamacion)
        return registro1 + ' - ' + registro2
