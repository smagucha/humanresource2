# Generated by Django 3.1.6 on 2021-05-01 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='PassportNo',
            field=models.CharField(max_length=50),
        ),
    ]
