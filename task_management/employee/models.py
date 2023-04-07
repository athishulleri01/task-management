from django.db import models
from add_employee.models import AddEmployee
from department.models import Department
# from main_task.models import MainTask
# Create your models here.

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    # emp_id = models.IntegerField(blank=True, null=True)
    emp=models.ForeignKey(AddEmployee,to_field='emp_id',on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    # dept_id = models.IntegerField(blank=True, null=True)
    dept=models.ForeignKey(Department,to_field='dept_id',on_delete=models.CASCADE)
    m_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


