# Generated by Django 3.1.6 on 2021-05-12 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20210512_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='remainingdays',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
