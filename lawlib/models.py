#新时代税费政策法规库/政府收入制度库
#New era tax policy warehouse
#本应用默认全部文件以2019年1月1日时为有效力状态。经过修订的文件，在标题后标记（**年版或**年第*版），没有修订过的，不做标记

from django.db import models
from datetime import date,timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

class Organization(models.Model):#定义发文机关
    formal_name  = models.CharField(max_length=40,verbose_name='发布机关',unique=True)#一般应使用规范化全称
    def __str__(self):
       return self.formal_name
    class Meta:
        verbose_name = '发文机关'
        verbose_name_plural = '发文机关'

class Fileprefix(models.Model):#定义发文代字，如"国务院令""财税""财预"等
    org_prefix = models.CharField(max_length=20,verbose_name='发文代字',unique=True)

    def __str__(self):
            return self.org_prefix
    class Meta:
        verbose_name = '发文代字'
        verbose_name_plural = '发文代字'

class Revenue(models.Model):#定义税费种
    revenue_name = models.CharField(max_length=40,verbose_name='税(费)名称',unique=True)
    def __str__(self):
             return self.revenue_name

    class Meta:
        verbose_name = '税费名称'
        verbose_name_plural = '税费名称'

class Document(models.Model):#定义政策文件结构
    GRADE_NAMES = (
            ('TT','税收协定'),#国家协议或条约，包括安排
            ('HH','税费法律'),#全国人民代表大会及其常委会制定的法律
            ('MH','行政法规'),#以国务院令发布或修订或确认的法规
            ('LH','中央政策'),#党中央、国务院发布（含同意发布）政策文件
            ('HM','地方性法规'),#地方各级立法机关制定的法规
            ('MM','司法解释'),#最高法、最高检制发的法律适用问题解释
            ('LM','部门规章'),#国务院部门及其直属机构以令形式发布规章
            ('HL','地方政府规章'),#省及省以下政府首长以令签发的规章
            ('ML','部委规范性文件'),#中央国家机关发布规范性文件
            ('LL','地方规范性文件'),#地方有法定职权机关发布规范性文件
            ('XX','其他文件'),#不在上述类别内的可反复适用的文件
            )
    grade = models.CharField(max_length=2, choices=GRADE_NAMES,verbose_name='法律层级',default='ML')
    revenue = models.ManyToManyField(Revenue,verbose_name='所涉及税（费）种',help_text="选择税（费）种名称,如未列出点旁边 ＋号增添,可多选")
    organization = models.ManyToManyField(Organization,verbose_name='发布机关',help_text="请输入发文机关,如未列出点旁边 ＋号增添,可多选")
    mdu = models.CharField(max_length=200,default='',null=True,blank=True,verbose_name='主送单位',help_text="除公告、通告以外的一般规范性文件需要输入主送单位")
    title = models.CharField(max_length=100,unique=True,verbose_name='法规名称',help_text="请输入文件标题,不需输入发文机关")
    fileprefix = models.ForeignKey(Fileprefix,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='发文代字',help_text="请选择发文代字,如未列出，点旁边 ＋号增添 ")
    file_order = models.CharField(max_length=20,default='〔20** 〕*号',null=True,blank=True,verbose_name='文件序号',help_text="请修改为正确的发文年份序号")
    reporter = models.CharField(max_length=40,null=True,blank=True,verbose_name='签发人',help_text="如有，请输入签发人")
    pub_date = models.DateField(verbose_name='签发日期',help_text="请输入文件正式签发日期,格式为英文输入状态下的 2019-1-1 ,下同。也可以点出旁边日历表选择")#文件正式签发日
    val_date = models.DateField(verbose_name='生效日期',help_text="请输入文件生效日期")#文件开始生效日
    dis_date = models.DateField(null=True,blank=True,verbose_name='失效日期',help_text="(可选)如有，请输入文件失效日期")#文件失去效力日
    repair = models.TextField(verbose_name='修订情况',default='',null=True,blank=True,help_text="（可选）输入文件历次修订情况")
    content_less = models.TextField(verbose_name='目录/前言',null=True,blank=True,help_text="（可选）不在此处输入条款具体规定内容")#文件约束性条款前的开头导语及文件章节结构等    
    content_tail = models.TextField(null=True,blank=True,verbose_name='文末/备注',help_text="(可选)输入一些强调性要求，个别特殊事项说明等内容")
    snapshot = models.URLField(verbose_name='官网文件链接',help_text="请输入文件官网链接,如为财政部文件，链接指向财政部发布该文件的网址;如为中共中央文件,输入国务院网站链接;找不到官网链接，输入本网站网址 http://taxagent.top 暂时代替")
    att_image = models.ImageField(upload_to='images',null=True,blank=True,verbose_name='（可选）如有，上传图表等附件')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document-detail', args=[str(self.id)])
    class Meta:
        ordering = ["pub_date"]
        verbose_name = '文件'
        verbose_name_plural = '文件'

class Provision(models.Model):#定义政策文件条文，由至少一款组成
    document = models.ForeignKey(Document,on_delete=models.CASCADE,verbose_name='所属文件',help_text="请选择正在输入或编辑条款所属文件")
    title = models.CharField(max_length=10,default='',verbose_name='条文序号',help_text="输入条的序号，比如'第一条' '一、'等，如没有此类序号，则按在正文中段序，如'第一段'")
    prov_order = models.AutoField(primary_key=True,verbose_name='存储主键',help_text="由数据库系统自动生成") 

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["prov_order"]
        verbose_name = '条(款)'
        verbose_name_plural = '条(款)'

    def get_absolute_url(self):
        return reverse('provision-detail', args=[str(self.prov_order)])

class Rule(models.Model):#定义政策文件条文，由至少一款组成
    rules = models.ForeignKey(Provision,on_delete=models.CASCADE,verbose_name='所属法条',help_text="请选择条款所属法条")
    ITEM_ATTRS = (         #定义条款规范内容，在实体、程序类下细分
       ('QYYW', '前言引文'),#立法目的之类内容
       ('JSFR', '缴税费人'),#纳税人和缴费人的统称
       ('ZSFW', '课征对象'),#征收范围的正列举
       ('BZDX', '不征对象'),#征收范围的反列举
       ('ZSPM', '征收品目'),#含细目
       ('SLFL', '税率费率'),#含征收率
       ('JSFS', '计算方式'),#包括计税公式、一般计税方法、简易计税方法之类
       ('MZYH', '免征优惠'),#无明确停止期限的优惠
       ('ZMYH', '暂免优惠'),#有明确执行期限的优惠
       ('SJJZ', '税基减征'),#含费种计征基础的减少确认条款
       ('SLJZ', '税率减征'),#含费率减少、征收上限设置等
       ('SEJZ', '税额减征'),#含费额的减征优惠
       ('SJZJ', '税基暂减'),#对税费计征基数的暂时性减计措施
       ('SLZJ', '税率暂减'),#新冠疫情期间，阶段性减小规模纳税人征收率即属此类
       ('SEZJ', '税额暂减'),#
       ('KJDM', '跨境抵免'),
       ('JNFS', '缴纳方式'),#含是否需要自行申报等
       ('JNHJ', '缴纳环节'),#含生产、消费环节缴纳等
       ('DZDK', '代征代扣'),#与缴纳环节有密切关联
       ('SBQX', '申报期限'),#申报期限与缴纳期限存在不一致的情形
       ('JNQX', '缴纳期限'),#包括明确的缴库条款
       ('JNDD', '缴纳地点'),
       ('ZFGL', '总分管理'),#含不设分支机构的外出经营事项
       ('YZYJ', '预征预缴'),#与总分管理有关联
       ('HSQJ', '汇算清缴'),
       ('TDJK', '退抵缴库'),#不含出口退税\留抵退税\即征即退
       ('CKTS', '出口退税'),
       ('LDTS', '留抵退税'),
       ('JZJT', '即征即退'),
       ('XZHF', '先征后返'),#属财政部门职责范围
       ('TBTZ', '特别调整'),
       ('xkrd', '许可认定'),#含与资格相关的登记
       ('SDFP', '税单发票'),#税务票证、税收凭证管理内容
       ('YHBL', '优惠办理'),#审批、备案、资料留存备查等
       ('XXBG', '信息报告'),#含纳税申报、缴费申报，税收身份报告等
       ('FWJC', '服务举措'),#税务机关义务
       ('CKCL', '财会处理'),#纳税人、缴费人的财务、帐务处理规定
       ('XXXT', '信息系统'),#财税部门关于信息系统、数据交换标准等规定
       ('BMXJ', '部门衔接'),#政府部门间在税费征缴职责中分工配合规定
       ('XYGL', '信用管理'),#含纳税信用管理和社会信用体系建设内容
       ('SWJC', '税务检查'),#含税务稽查、纳税评估、风险分析等
       ('XZQZ', '行政强制'),#含行政强制措施与行政强制执行
       ('XZCF', '行政处罚'),#含暂停出口退税资格、停供发票
       ('FLJJ', '法律救济'),
       ('ZCCL', '追责处理'),#行政机关人员或其行政相对人的法律责任
       ('ZXRQ', '执行日期'),
       ('LFSQ', '立法授权'),
       ('HHLX', '混合类型'),
       ('QTGD', '其他规定'),
       )
    item_attr = models.CharField(max_length=4, choices=ITEM_ATTRS,default='JSFS',verbose_name='规制重点',help_text="请选择条款内容属性")
    WHO_DUTY = (
              ('G','政府部门'),
              ('M','市场主体'),
              ('F','混合类型'),
              )
    duty = models.CharField(max_length=1, choices=WHO_DUTY, default='M',  verbose_name='义务归属方', help_text='请选择该条需何方履行义务')
    VALID_STATES = (
            ('I','初始有效'),#条款保持初次发布有效状态
            ('F','修订有效'),#条款经过至少一次修订且有效
            ('P','暂停执行'),#条款被有权部门宣布暂停执行
            ('A','恢复执行'),#原暂停执行的条款恢复执行
            ('D','条款失效'),#条款被有权部门宣布非暂时性失效
            ('Z','模糊待定'),#因各有关规定间冲突等效力待定
            )
    status = models.CharField(max_length=1, choices=VALID_STATES, default='I',verbose_name='生效状态', help_text='请选择该条款当前效力状态')
    val_date = models.DateField(default='2019-1-1',verbose_name='条款开始生效期')#条款开始生效日
    dis_date = models.DateField(null=True,blank=True,verbose_name='(可选)条款失效日期')#条款因删改失效日
    content = models.TextField(default='',verbose_name='本款内容',help_text="如仅有一段，第一段即为该款全部内容，下面不需要再输入")

    def __str__(self):
            return self.content

    class Meta:
        verbose_name = '款'
        verbose_name_plural = '款'

class TaxReturn(models.Model):
    revenue = models.ForeignKey(Revenue,on_delete=models.CASCADE,null=True,verbose_name='对应税(费)种',help_text="选择申报表所对应的税(费)种名称")
    title = models.CharField(max_length=100,default='**申报表(20xx年版)',verbose_name='申报表名称',help_text="请输入纳税申报表名称,将版本号附在名称后的括号内")
    val_date = models.DateField(default='2019-1-1',verbose_name='启用日期',help_text="输入该版本申报表从哪天开始使用")
    dis_date = models.DateField(null=True,blank=True,verbose_name='停用日期',help_text="输入该版本申报表从哪天开始不可用")
    base_file = models.CharField(max_length=100,default='税务总局关于**公告（税务总局公告20xx第x号）',verbose_name='启用申报表文件',help_text="请修改为正确的明确该申报表样式、使用日期等启用事项的文件名称")
    base_file_url = models.URLField(verbose_name='官网链接',help_text="请输入上述文件的官网链接")
    fill_form = models.TextField(verbose_name='表格内容',help_text="请粘贴申报表HTML代码，可用wps-office可从doc/xls等文档转存得到")
    fill_info = models.TextField(verbose_name='填表说明',help_text="请输入官方发布的申报表填写说明")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('taxreturn-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = '申报表'
        verbose_name_plural = '申报表'
