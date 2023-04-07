from django.db import models

# Create your models here.
class NotificationManager(models.Model):
    nm_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    fille_attach = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_manager'

