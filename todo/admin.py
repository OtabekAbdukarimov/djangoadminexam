from todo.models import *
from django.contrib import admin
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)

#
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "qty", "price")


    def has_delete_permission(self, request, obj=None):
        if obj and obj.qty != 0:
            return False
        else:
            return True





@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "product_name", "qty", "summa", "created_at")

    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("title", "phone", "product_count", "address")

    def has_delete_permission(self, request, obj=None):
        if obj and obj.product_count != 0:
            return False
        else:
            return True
    def product_count(self, obj):
        products = Product.objects.filter(company=obj)
        quantity = 0
        for product in products:
            quantity += product.qty
        return quantity



    product_count.short_description = "mahsulotlari soni"