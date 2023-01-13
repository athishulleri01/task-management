from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    u_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


