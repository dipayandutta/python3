# Generated by Django 3.2.4 on 2021-06-14 18:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('excerpt', models.TextField(null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
        ),
    ]
