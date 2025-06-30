from django.db import models

class ProductBid(models.Model):
    product_id = models.CharField(max_length=100)
    current_cpc = models.DecimalField(max_digits=10, decimal_places=2)
    target_roas = models.DecimalField(max_digits=5, decimal_places=2)
    adjusted_cpc = models.DecimalField(max_digits=10, decimal_places=4)
    submitted_at = models.DateTimeField(auto_now_add=True)
    calculated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["calculated_at", "product_id"], name="idx_calc_product"),
        ]