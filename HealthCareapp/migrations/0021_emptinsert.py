# Generated by Django 3.2.4 on 2022-01-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCareapp', '0020_delete_sig'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmptInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
