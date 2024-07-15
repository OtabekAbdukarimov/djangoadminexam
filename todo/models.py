from django.db import models

class Product(models.Model):
    title = models.CharField(verbose_name="Mahsulot nomi", max_length=125)
    company = models.ForeignKey("todo.Company", on_delete=models.CASCADE)
    price = models.PositiveIntegerField("narxi")
    qty = models.PositiveIntegerField("soni")

    def __str__(self):
        return self.title

class Company(models.Model):
    title = models.CharField(verbose_name="Kompaniya nomi", max_length=100)
    phone = models.CharField(verbose_name="telefon raqami", max_length=15)
    address = models.CharField(verbose_name="manzil", max_length=200)
    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.title



class Sale(models.Model):
    customer_name = models.CharField(verbose_name="xaridor ismi", max_length=150)
    product_name = models.ForeignKey("todo.Product", verbose_name="mahsulot nomi", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(verbose_name="soni")
    summa = models.PositiveIntegerField(verbose_name="umumiy narxi", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)




    def save(self, *args, **kwargs):
        if not self.id:
            try:
                product = self.product_name
                if product.qty >= self.qty:
                    product.qty -= self.qty
                    self.summa = product.price * self.qty
                    product.save()
                else:
                    raise ValueError("Yetarli miqdor mavjud emas")
            except Product.DoesNotExist:
                raise ValueError("Tanlangan mahsulot mavjud emas")

        super().save(*args, **kwargs)
