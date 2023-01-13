from django.db import models

# Create your models here.
class VideoConference(models.Model):
    video_conference_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    video_conference = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_conference'

