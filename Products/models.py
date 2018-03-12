from django.db import models


class MedicalProduct(models.Model):
    no = models.CharField(max_length=16, verbose_name=u'编码')
    name = models.CharField(max_length=255, verbose_name=u'名称')
    norms = models.CharField(max_length=50, verbose_name=u'规格', blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'单位')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=u'单价')
    tax = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=u'税')
    stock_num = models.IntegerField(default=0, verbose_name=u'库存')
    sold_num = models.IntegerField(default=0, verbose_name=u'已售出')
    batch = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'生产批号')
    reg_no = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'注册证号')
    producers = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'生产企业')
    valid = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'有效期')
    storage_time = models.DateTimeField(auto_now_add=True, verbose_name=u'入库时间')
    product_type = models.SmallIntegerField(default=0)  # 类别

    class Meta:
        db_table = 'medical_product'
        ordering = ['-id']
