# Generated by Django 3.2.4 on 2022-01-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCareapp', '0023_auto_20220103_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='SymptoInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(max_length=150)),
                ('s2', models.CharField(max_length=150)),
                ('s3', models.CharField(max_length=150)),
                ('s4', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='SymptomInsert',
        ),
    ]
