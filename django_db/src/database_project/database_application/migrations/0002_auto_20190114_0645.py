# Generated by Django 2.0.7 on 2019-01-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.CharField(default='Summary', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]