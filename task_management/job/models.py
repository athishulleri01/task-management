from django.db import models

# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    desi_id = models.IntegerField(blank=True, null=True)
    dep_id = models.IntegerField(blank=True, null=True)
    noof_post = models.IntegerField(blank=True, null=True)
    job_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'

