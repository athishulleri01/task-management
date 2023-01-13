from django.db import models
from employee_reg.models import EmpRegister
# Create your models here.

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    # emp_id = models.IntegerField(blank=True, null=True)
    emp=models.ForeignKey(EmpRegister,to_field='emp_id',on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    dept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


