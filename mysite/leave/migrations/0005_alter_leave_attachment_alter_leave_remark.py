# Generated by Django 4.1.3 on 2023-01-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0004_leave_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='attachment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]