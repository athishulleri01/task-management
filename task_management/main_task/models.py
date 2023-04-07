from django.db import models
from employee.models import AddEmployee
# Create your models here.
class MainTask(models.Model):
    mt_id = models.AutoField(primary_key=True)
    # emp_id = models.IntegerField(blank=True, null=True)
    emp=models.ForeignKey(AddEmployee,to_field='emp_id',on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    file_attach = models.TextField(blank=True, null=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    m_status = models.CharField(max_length=45, blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    feed_date = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    sum_date = models.DateTimeField(blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)
    task_manager_id = models.IntegerField(blank=True, null=True)
    # task_manager = models.ForeignKey(AddEmployee, to_field='emp_id', on_delete=models.CASCADE)
    # tskMng = models.ForeignKey(AddEmployee, to_field='task_manager', on_delete=models.CASCADE)
    task_asign_tm_date = models.DateTimeField(blank=True, null=True)
    task_deadline_tm_date = models.DateTimeField(blank=True, null=True)
    task_due_tm_date = models.DateTimeField(blank=True, null=True)
    task_mng_desc = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    task_mngr_nm = models.CharField(max_length=45, blank=True, null=True)
    tskmgr_submit = models.CharField(max_length=300, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'main_task'
