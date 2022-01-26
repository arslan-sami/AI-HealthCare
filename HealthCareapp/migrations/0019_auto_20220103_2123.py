# Generated by Django 3.2.4 on 2022-01-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCareapp', '0018_rename_tasktitle_task_tasktitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('phone_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]