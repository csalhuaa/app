from django.db import models

from .Sale import Sale

class Payment(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"Payment #{self.pk}"