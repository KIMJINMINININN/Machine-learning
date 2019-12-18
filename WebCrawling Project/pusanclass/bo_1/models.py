from django.db import models

class B_list(models.Model):
    objects       = models.Manager()
    id_no         = models.AutoField(primary_key=True)
    title         = models.CharField(max_length=100,null=True, default ='')
    number        = models.TextField(null=True, default ='')
    addressroad   = models.TextField(null=True, default ='')
    addressgi     = models.TextField(null=True, default ='')
    opentime      = models.TextField(null=True, default ='')
    pageaddress   = models.TextField(null=True, default ='')
    info          = models.TextField(null=True, default ='')
    ellipsis_area = models.TextField(null=True, default ='')
    image         = models.BinaryField(null=True)
    def __str__(self):
        return str(self.title+','+self.number+','+self.addressroad+','+self.addressgi+','+self.opentime+','+self.pageaddress+','+self.info+','+self.ellipsis_area+','+self.image)

