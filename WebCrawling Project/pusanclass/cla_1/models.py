from django.db import models

# Create your models here.
class List(models.Model):
    objects     = models.Manager()
    id          = models.CharField(max_length=30, primary_key =True)
    title       = models.TextField()
    date        = models.TextField()
    content     = models.TextField(null=True, default ='')
    def __str__(self):
        return str(self.id+','+self.title+','+self.date+'.'+self.content)
