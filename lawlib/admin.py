from django.contrib import admin
from .models import Organization,Fileprefix,Revenue,Document,Provision,Rule,TaxReturn
# Register your models here.

#class RuleInline(admin.StackedInline):
class RuleInline(admin.TabularInline):
#class RuleInline(admin.StackedInline):
    model = Rule
    extra = 0

#class ProvisionInline(admin.StackedInline):
#    model = Provision
#    extra = 1

class ProvisionAdmin(admin.ModelAdmin):
    inlines = [RuleInline]
    list_display = ('document','title','prov_order',)
#    search_fields = ['rule']

class DocumentAdmin(admin.ModelAdmin):
#    fieldsets = [
#            (None,       {'fields':['title']}),
#            ('时效信息', {'fields':['pub_date','val_date']}),
#            ('内容信息', {'fields':['content_less']})
#            ]        
#    inlines = [ProvisionInline] 
    list_display = ('title','grade','pub_date','val_date','content_less')
    list_filter = ['revenue','grade',]
#    radio_fields = {'revenue':admin.VERTICAL}

class TaxReturnAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document,DocumentAdmin)
admin.site.register(Provision,ProvisionAdmin)
#admin.site.register(Rule)
admin.site.register(Organization)
admin.site.register(Fileprefix)
admin.site.register(Revenue)
admin.site.register(TaxReturn,TaxReturnAdmin)
