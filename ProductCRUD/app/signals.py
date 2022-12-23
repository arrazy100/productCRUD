from django.db.models.signals import pre_save

from .models import (ProductModel)
from .util import generateCode

def pre_save_product(sender, instance, **kwargs):
    if (not instance.pk):
        if (instance.code):
            try:
                product = ProductModel.objects.get(code = instance.code)
                code = int(instance.code) + 1
                instance.code = str(code)
            except ProductModel.DoesNotExist:
                print(f'Code {instance.code} not used by any product, no increment')
        else:
            instance.code = generateCode(8)

pre_save.connect(
    pre_save_product,
    sender=ProductModel,
    dispatch_uid='generate_code_for_product'
)