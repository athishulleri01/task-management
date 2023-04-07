from django.db import models

# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    complaint = models.CharField(max_length=500, blank=True, null=True)
    reply = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    replay_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint'


