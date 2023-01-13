from django.db import models

# Create your models here.
class Call(models.Model):
    call_id = models.AutoField(primary_key=True)
    contact = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call'

