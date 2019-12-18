from django.db import models


# Create your models here.

class Join(models.Model):
    objects = models.Manager()
    id      = models.CharField(max_length=30, primary_key=True)
    pw      = models.CharField(max_length=100)
    name    = models.CharField(max_length=100,null=True, default ='')
    tel     = models.CharField(max_length=100,null=True, default ='')
    email   = models.CharField(max_length=100,null=True, default ='')
    date    = models.DateTimeField(auto_now_add = True)  #DATE
    def __str__(self):
        return str(self.id+','+self.pw+','+self.name+','+self.tel+','+self.email+','+self.date)


    

   
    