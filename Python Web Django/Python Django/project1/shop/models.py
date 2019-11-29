from django.db import models

# Create your models here.
class Item(models.Model):
    objects = models.Manager()
    itm_no = models.AutoField(primary_key=True)
    itm_name = models.CharField(max_length=100)
    itm_content = models.TextField()
    itm_price = models.IntegerField()
    itm_qty = models.IntegerField()
    itm_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.itm_no)

