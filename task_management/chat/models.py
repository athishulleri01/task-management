from django.db import models

# Create your models here.
class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    m_id = models.IntegerField(blank=True, null=True)
    chat = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    reply = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat'
