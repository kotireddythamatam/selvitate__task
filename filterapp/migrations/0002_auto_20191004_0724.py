# Generated by Django 2.1.7 on 2019-10-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='Price',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='Review_Count',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='Reviews',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
