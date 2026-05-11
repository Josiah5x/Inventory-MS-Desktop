# thisset = {"apple", "banana", "cherry", "apple", "apple"}

# print(thisset)

# from django.db import models

# # Create your models here.
# from django.db import models

# class Product(models.Model):

#     product_code = models.CharField(max_length=50, unique=True)
#     product_name = models.CharField(max_length=255)
#     secondary_name = models.CharField(max_length=255, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     type = models.CharField(max_length=20)
#     vat_category = models.CharField(max_length=50)
#     unit = models.CharField(max_length=20)
#     selling_price = models.DecimalField(max_digits=10, decimal_places=2)
#     selling_currency = models.CharField(max_length=10)
#     brand = models.CharField(max_length=100, blank=True, null=True)
#     family = models.CharField(max_length=100, blank=True, null=True)
#     sub_family = models.CharField(max_length=100, blank=True, null=True)
#     shelf_no = models.CharField(max_length=50, blank=True, null=True)
#     supplier = models.CharField(max_length=255)
#     supplier_item_code = models.CharField(max_length=100, blank=True, null=True)
#     supplier_price = models.DecimalField(max_digits=10, decimal_places=2)
#     supplier_currency = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.product_name} {self.product_code}"

# class PurchaseInvoice(models.Model):
#     purchase_code = models.CharField(max_length=250)
#     purchase_year = models.CharField(max_length=200)
#     purchase_number = models.CharField(max_length=200)
#     doc_date = models.CharField(max_length=200)
#     supplier = models.CharField(max_length=200)
#     currency = models.CharField(max_length=200)
#     credits_fercility = models.CharField(max_length=200)
#     # 
# class PurchaseInvoiceItems(models.Model):
#     product_code = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     warehouse = models.CharField(max_length=100)
#     cost_center = models.CharField(max_length=100)
#     quantity = models.FloatField()
#     unit = models.CharField(max_length=20)
#     unit_price = models.FloatField()
#     amount = models.FloatField(blank=True, null=True)
#     discount_percentage = models.FloatField(default=0)
#     discount = models.FloatField(blank=True, null=True)
#     vat_percentage = models.FloatField(default=0)
#     net_amount = models.FloatField(blank=True, null=True)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 
}
for k in thisdict:
    if thisdict[k] == "" or 0:
        print(k)
    
# print(hinforDic["doc_code"])
        # print(hinforDic["doc_year"])
        # print(hinforDic["doc_num"])
        # print(hinforDic["doc_date"])
        # print(hinforDic["supplier_name"])
        # print(hinforDic["supplier_num"])
        # print(hinforDic["currency"])
        # print(hinforDic["credit_f"])