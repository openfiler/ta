# Generated by Django 3.0.3 on 2020-03-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0023_document_mdu'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='repair',
            field=models.TextField(blank=True, default='', help_text='（可选）输入文件历次修订情况', null=True, verbose_name='修订情况'),
        ),
    ]