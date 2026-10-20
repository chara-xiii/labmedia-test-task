from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
 
    class Meta:
        db_table = 'clients'
 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Payment(models.Model):
    payer = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    percent = models.IntegerField()
    pay_date = models.DateTimeField()
 
    class Meta:
        db_table = 'payments'
        ordering = ['pay_date']
 
    def __str__(self):
        return f'Payment #{self.pk} - {self.amount}'

