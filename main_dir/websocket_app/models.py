from django.db import models


# Create your models here.
class BTCModel(models.Model):
    """
    Bitcoin Model
    """
    priceUsd = models.DecimalField(max_digits=9, decimal_places=2)
    time = models.BigIntegerField()
    data = models.DateTimeField()

    def __str__(self):
        return f'{str(self.data)}: {self.priceUsd}'
