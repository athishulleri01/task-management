from django.db import models

# Create your models here.
class NotificationAdmin(models.Model):
    na_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    tile = models.CharField(max_length=45, blank=True, null=True)
    file_attach = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    who = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_admin'

