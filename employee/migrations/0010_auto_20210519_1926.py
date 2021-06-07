# Generated by Django 3.1.6 on 2021-05-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20210515_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='leavedays',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='remainingdays',
        ),
        migrations.AlterField(
            model_name='leave',
            name='approved',
            field=models.CharField(blank=True, choices=[('sick', 'sick'), ('Maternity', 'Maternity'), ('Paternity', 'Paternity'), ('bereavement', 'bereavement'), ('bereavement', 'bereavement'), ('unpaid', 'unpaid'), ('approved', 'approved'), ('notapproved', 'notapproved')], default='notapproved', max_length=11, null=True),
        ),
    ]