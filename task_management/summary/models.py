from django.db import models
from main_task.models import MainTask
# Create your models here.
class Summary(models.Model):
    summary_id = models.AutoField(primary_key=True)
    mt_id = models.IntegerField(blank=True, null=True)
    # mtid=models.ForeignKey(MainTask,on_delete=models.CASCADE)
    m_id = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summary'
