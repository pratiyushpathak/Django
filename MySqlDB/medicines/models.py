from django.db import models


class Medicines(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=100)
    m_expiery = models.DateField()
    m_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'medicines'

    def __str__(self):
        return self.m_name