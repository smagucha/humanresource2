# Generated by Django 3.1.6 on 2021-05-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_leave_remainingdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='remainingdays',
            field=models.PositiveIntegerField(blank=True, default=models.PositiveIntegerField(default=30), null=True),
        ),
    ]
