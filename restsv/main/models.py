from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'restsv_parts'
        verbose_name = '配件'
        verbose_name_plural = '配件表'

class Brand(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'restsv_brands'
        verbose_name = '品牌'
        verbose_name_plural = '品牌表'

class Model(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'restsv_models'
        verbose_name = '型号'
        verbose_name_plural = '型号表'
