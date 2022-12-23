from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def get_products(self):
        return ProductModel.objects.filter(categoryId=self.id)

class ProductModel(models.Model):
    code = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    categoryId = models.ForeignKey(CategoryModel, on_delete=models.CASCADE);