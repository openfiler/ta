# Generated by Django 3.0.3 on 2020-03-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0022_auto_20200306_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='mdu',
            field=models.CharField(blank=True, default='', help_text='除公告、通告以外的一般规范性文件需要输入主送单位', max_length=200, null=True, verbose_name='主送单位'),
        ),
    ]
