# Generated by Django 3.0.3 on 2020-03-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0010_auto_20200303_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterModelOptions(
            name='provision',
            options={'ordering': ['prov_order']},
        ),
    ]
