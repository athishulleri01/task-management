from django.db import models

# Create your models here.
class Designation(models.Model):
    desi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    rank = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designation'

