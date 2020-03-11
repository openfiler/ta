# Generated by Django 3.0.3 on 2020-03-02 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0005_auto_20200302_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileprefix',
            name='org_prefix',
            field=models.CharField(max_length=20, unique=True, verbose_name='发文代字'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='formal_name',
            field=models.CharField(max_length=40, unique=True, verbose_name='发布机关'),
        ),
        migrations.AlterField(
            model_name='provision',
            name='title',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='条文序号'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='revenue_name',
            field=models.CharField(max_length=40, unique=True, verbose_name='税（费）名称'),
        ),
    ]