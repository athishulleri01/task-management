from django.db import models

# Create your models here.
class Manager(models.Model):
    m_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    dept_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'
