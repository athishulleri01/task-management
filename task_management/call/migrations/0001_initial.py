# Generated by Django 3.2.15 on 2023-01-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('call_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'call',
                'managed': False,
            },
        ),
    ]