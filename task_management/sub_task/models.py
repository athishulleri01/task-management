from django.db import models
from add_employee.models import AddEmployee
from manager.models import Manager
from main_task.models import MainTask
# Create your models here.
class SubTask(models.Model):
    st_id = models.AutoField(primary_key=True)
    # m_id = models.IntegerField(blank=True, null=True)
    # m = models.ForeignKey(Manager,to_field='m_id',on_delete=models.CASCADE)
    # emp_id = models.IntegerField(blank=True, null=True)
    emp = models.ForeignKey(AddEmployee, to_field='emp_id', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    # start_date = models.DateTimeField(blank=True, null=True)
    # end_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    file_attach = models.TextField(blank=True, null=True)
    # st_status = models.CharField(max_length=45, blank=True, null=True)
    # feedback = models.CharField(max_length=500, blank=True, null=True)
    # feed_date = models.DateTimeField(blank=True, null=True)
    # rating = models.IntegerField(blank=True, null=True)
    # m_task = models.CharField(max_length=45, blank=True, null=True)
    # emp_data = models.CharField(max_length=45, blank=True, null=True)
    # mt_id = models.IntegerField(blank=True, null=True)
    mt= models.ForeignKey(MainTask, to_field='mt_id', on_delete=models.CASCADE)
    # emp_id = models.IntegerField(blank=True, null=True)
    tm_id = models.IntegerField(blank=True, null=True)
    # mt_id = models.IntegerField(blank=True, null=True)
    assign_date = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    s_description = models.CharField(max_length=5000, blank=True, null=True)
    s_submit_date = models.DateTimeField(blank=True, null=True)
    s_submit_time = models.TimeField(blank=True, null=True)
    s_file_attach1 = models.CharField(max_length=200, blank=True, null=True)
    s_file_attach2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_task'
