from django.db import models


# Create your models here.


class Baijiaxing(models.Model):
    surname = models.CharField(max_length=255)
    name_url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'baijia'
