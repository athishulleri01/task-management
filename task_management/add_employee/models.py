from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=45, blank=True, null=True)
    qualification = models.CharField(max_length=45, blank=True, null=True)
    experience = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=45, blank=True, null=True)
    dob = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    join_date = models.DateTimeField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_employee'
