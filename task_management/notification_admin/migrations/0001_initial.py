# Generated by Django 3.2.15 on 2023-01-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationAdmin',
            fields=[
                ('na_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_id', models.IntegerField(blank=True, null=True)),
                ('m_id', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('tile', models.CharField(blank=True, max_length=45, null=True)),
                ('file_attach', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'notification_admin',
                'managed': False,
            },
        ),
    ]
