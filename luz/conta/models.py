from django.db import models


class Conta(models.Model):
    date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    mw = models.FloatField()

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y")} {self.amount_paid} {self.mw}'
