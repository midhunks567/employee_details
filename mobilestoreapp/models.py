
from django.db import models

# Create your models here.
from django.urls import reverse


class Brand_nm(models.Model):
    brand_name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        db_table:'phone_brand'

    def get_url(self):
        return reverse('prod_brand',args=[self.slug])

    def __str__(self):
        return self.brand_name

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    price=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='pictures')
    brand_name=models.ForeignKey(Brand_nm,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('details', args=[self.brand_name.slug, self.slug])



