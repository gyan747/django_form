# Generated by Django 4.0.1 on 2022-02-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_stock_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
