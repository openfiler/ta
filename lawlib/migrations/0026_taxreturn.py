# Generated by Django 3.0.3 on 2020-03-07 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0025_auto_20200307_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tilte', models.CharField(default='**申报表(20xx年版)', help_text='请输入纳税申报表名称,将版本号附在名称后的括号内', max_length=100, verbose_name='申报表名称')),
                ('val_date', models.DateField(default='2019-1-1', help_text='输入该版本申报表从税款属期最早哪天可用', verbose_name='使用属期起')),
                ('dis_date', models.DateField(blank=True, help_text='输入该版本申报表从税款属期最迟哪天不可用', null=True, verbose_name='使用属期止')),
                ('base_file', models.CharField(default='税务总局关于**申报表**通知（税总*〔20xx 〕x号）', help_text='请修改为正确的明确该申报表样式、使用日期等启用事项的文件名称', max_length=100, verbose_name='启用申报表文件')),
                ('base_file_url', models.URLField(help_text='请输入上述文件的官网链接', verbose_name='官网链接')),
                ('fill_form', models.TextField(help_text='请粘贴申报表HTML代码，用wps可从doc/xls等文档转存得到', verbose_name='表格内容')),
                ('fill_info', models.TextField(help_text='请输入官方发布的申报表填写说明', verbose_name='填表说明')),
                ('revenue', models.ForeignKey(help_text='选择申报表所对应的税(费)种名称', null=True, on_delete=django.db.models.deletion.CASCADE, to='lawlib.Revenue', verbose_name='对应税(费)种')),
            ],
            options={
                'verbose_name': '申报表',
                'verbose_name_plural': '申报表',
            },
        ),
    ]
