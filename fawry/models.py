from django.db import models

# Create your models here.
class Fawry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    money_borrowed = models.DecimalField(max_digits=10, decimal_places=2)
    money_payed_back = models.DecimalField(max_digits=10, decimal_places=2)
    difference = models.DecimalField(max_digits=10 , decimal_places=2 , default=0)


class Transaction(models.Model):
    PAYMENT_CHOICES = (
        ('كاش', 'كاش'),
        ('فوري', 'فوري'),
    )
    fawry = models.ForeignKey(Fawry, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.CharField(max_length=10, choices=PAYMENT_CHOICES ,default=1)

class user(models.Model):
    total_money  =models.DecimalField(max_digits=15 , decimal_places=2 , default=0)


