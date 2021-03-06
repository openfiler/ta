# Generated by Django 3.0.3 on 2020-03-10 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawlib', '0029_auto_20200308_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='item_attr',
            field=models.CharField(choices=[('QYYW', '前言引文'), ('JSFR', '缴税费人'), ('ZSFW', '课征对象'), ('BZDX', '不征对象'), ('ZSPM', '征收品目'), ('SLFL', '税率费率'), ('JSFS', '计算方式'), ('MZYH', '免征优惠'), ('ZMYH', '暂免优惠'), ('SJJZ', '税基减征'), ('SLJZ', '税率减征'), ('SEJZ', '税额减征'), ('SJZJ', '税基暂减'), ('SLZJ', '税率暂减'), ('SEZJ', '税额暂减'), ('KJDM', '跨境抵免'), ('JNFS', '缴纳方式'), ('JNHJ', '缴纳环节'), ('DZDK', '代征代扣'), ('SBQX', '申报期限'), ('JNQX', '缴纳期限'), ('JNDD', '缴纳地点'), ('ZFGL', '总分管理'), ('YZYJ', '预征预缴'), ('HSQJ', '汇算清缴'), ('TDJK', '退抵缴库'), ('CKTS', '出口退税'), ('LDTS', '留抵退税'), ('JZJT', '即征即退'), ('XZHF', '先征后返'), ('TBTZ', '特别调整'), ('xkrd', '许可认定'), ('SDFP', '税单发票'), ('YHBL', '优惠办理'), ('XXBG', '信息报告'), ('FWJC', '服务举措'), ('CKCL', '财会处理'), ('XXXT', '信息系统'), ('BMXJ', '部门衔接'), ('XYGL', '信用管理'), ('SWJC', '税务检查'), ('XZQZ', '行政强制'), ('XZCF', '行政处罚'), ('FLJJ', '法律救济'), ('ZCCL', '追责处理'), ('ZXRQ', '执行日期'), ('LFSQ', '立法授权'), ('HHLX', '混合类型'), ('QTGD', '其他规定')], default='JSFS', help_text='请选择条款内容属性', max_length=4, verbose_name='规制重点'),
        ),
        migrations.AlterField(
            model_name='taxreturn',
            name='dis_date',
            field=models.DateField(blank=True, help_text='输入该版本申报表从哪天开始不可用', null=True, verbose_name='停用日期'),
        ),
        migrations.AlterField(
            model_name='taxreturn',
            name='val_date',
            field=models.DateField(default='2019-1-1', help_text='输入该版本申报表从哪天开始使用', verbose_name='启用日期'),
        ),
    ]
