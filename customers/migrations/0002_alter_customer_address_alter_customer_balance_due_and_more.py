# Generated by Django 4.1.7 on 2023-09-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ADDRESS',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='BALANCE_DUE',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CONTACT',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='STATUS',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
