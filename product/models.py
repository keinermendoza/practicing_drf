from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5,
                              decimal_places=2,
                              default=50.25)
    
    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 1.12)

    def get_discount(self):
        return '%.2f' %(float(self.price) / 2)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['price']