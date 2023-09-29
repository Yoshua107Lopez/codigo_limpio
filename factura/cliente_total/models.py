from django.db import models

# Modelo
from django.db import models

class data(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_cliente': self.nombre_cliente,
            'total': str(self.total),
        }
