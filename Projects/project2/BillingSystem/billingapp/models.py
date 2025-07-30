from django.db import models

# Create your models here.
class BillingRecord(models.Model):
    customer_name = models.CharField(max_length=255)
    product_list = models.JSONField(default=list)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateTimeField(auto_now_add=True)