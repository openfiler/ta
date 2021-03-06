# Generated by Django 3.0.3 on 2020-03-04 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0015_auto_20200304_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='att_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='（可选）如有，上传图表等附件'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_less',
            field=models.TextField(help_text='（可选）不在此处输入条款具体规定内容', verbose_name='文头/前言'),
        ),
        migrations.AlterField(
            model_name='document',
            name='content_tail',
            field=models.TextField(blank=True, help_text='(可选)输入一些强调性要求，个别条款的特别执行期间等内容', null=True, verbose_name='文末/备注'),
        ),
        migrations.AlterField(
            model_name='document',
            name='dis_date',
            field=models.DateField(blank=True, help_text='(可选)如有，请输入文件失效日期', null=True, verbose_name='失效日期'),
        ),
        migrations.AlterField(
            model_name='document',
            name='file_order',
            field=models.CharField(blank=True, default='〔20** 〕*号', help_text='请修改为正确的发文年份序号', max_length=20, null=True, verbose_name='文件序号'),
        ),
        migrations.AlterField(
            model_name='document',
            name='organization',
            field=models.ManyToManyField(help_text='请输入发文机关,如未列出点旁边 ＋号增添,可多选', to='lawlib.Organization', verbose_name='发布机关'),
        ),
        migrations.AlterField(
            model_name='document',
            name='pub_date',
            field=models.DateField(help_text='请输入文件正式签发日期,格式为英文输入状态下的 2019-1-1 ,下同。也可以点出旁边日历表选择', verbose_name='签发日期'),
        ),
        migrations.AlterField(
            model_name='document',
            name='revenue',
            field=models.ManyToManyField(help_text='选择税（费）种名称,如未列出点旁边 ＋号增添,可多选', to='lawlib.Revenue', verbose_name='所涉及税（费）种'),
        ),
        migrations.AlterField(
            model_name='document',
            name='snapshot',
            field=models.URLField(help_text='请输入文件官网链接,如为财政部文件，链接指向财政部发布该的网址', verbose_name='官网文件链接'),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(help_text='请输入文件标题,不需输入发文机关', max_length=100, unique=True, verbose_name='法规名称'),
        ),
        migrations.AlterField(
            model_name='provision',
            name='document',
            field=models.ForeignKey(help_text='请选择正在输入或编辑条款所属文件', on_delete=django.db.models.deletion.CASCADE, to='lawlib.Document', verbose_name='所属文件'),
        ),
        migrations.AlterField(
            model_name='provision',
            name='title',
            field=models.CharField(default='', help_text="输入条的序号，比如'第一条' '一、'等，如没有按在正文中段序，如'第一段'", max_length=10, verbose_name='条文序号'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='dis_date',
            field=models.DateField(blank=True, null=True, verbose_name='(可选)条款失效日期'),
        ),
    ]
