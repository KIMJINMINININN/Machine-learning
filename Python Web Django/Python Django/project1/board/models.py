from django.db import models

# Create your models here.
class Board(models.Model):
    objects = models.Manager()
    br_no = models.AutoField(primary_key=True)
    br_title = models.CharField(max_length=100)
    br_content = models.TextField()
    br_writer = models.TextField()
    br_hit = models.IntegerField()
    br_date = models.DateField(auto_now_add=True)
    br_img = models.ImageField(blank=True)

    def __str__(self):
        return str(self.br_no) #문자만 가능
