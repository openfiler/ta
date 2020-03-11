# Generated by Django 3.0.3 on 2020-03-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0004_auto_20200302_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provision',
            name='prov_order',
            field=models.SmallAutoField(help_text='由数据库系统自动生成', primary_key=True, serialize=False, verbose_name='存储主键'),
        ),
        migrations.AlterField(
            model_name='provision',
            name='title',
            field=models.CharField(default='', max_length=10, verbose_name='条文序号'),
        ),
    ]
