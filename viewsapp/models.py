from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    ceo = models.CharField(max_length=80)
    origin_date = models.IntegerField()
    origin_place = models.CharField(max_length=80)
    logo = models.ImageField(upload_to='logo',blank=True,null=True)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("detail",kwargs={"pk":self.pk})

class Products(models.Model):
    company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    mielage = models.IntegerField()
    tank_capacity = models.FloatField(max_length=20)
    colour = models.CharField(max_length=25)
    price = models.IntegerField()
    cc = models.FloatField()
    pimage = models.ImageField(upload_to='pimage',blank=True,null=True)

    def __str__(self):
        return self.product_name
