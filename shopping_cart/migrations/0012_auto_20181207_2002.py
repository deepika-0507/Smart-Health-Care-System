# Generated by Django 2.0.5 on 2018-12-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0011_auto_20181207_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='patient_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_phno',
            field=models.IntegerField(null=True),
        ),
    ]