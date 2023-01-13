from django.db import models
from manager.models import Manager
# Create your models here.
class MainTask(models.Model):
    mt_id = models.AutoField(primary_key=True)
    # m_id = models.IntegerField(blank=True, null=True)
    m=models.ForeignKey(Manager,to_field='m_id',on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    file_attach = models.TextField(blank=True, null=True)
    current_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    m_status = models.CharField(max_length=45, blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    feed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_task'

