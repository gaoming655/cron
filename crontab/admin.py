from django.contrib  import admin
from crontab.models import *
from simple_history.admin import SimpleHistoryAdmin



class ListCrond(admin.ModelAdmin):
    list_display=('id','project','usage','conn_db','min','hour','month','week','day','program','program_ip','influence','status','date')
    ordering=('date',)
    list_filter = ('date',)
    exclude = ('date',)
    def get_min(self,obj):
    	return "\n".join([p.var for p in obj.min.all()])
    def get_hour(self,obj):
    	return "\n".join([p.var for p in obj.hour.all()])
    def get_day(self,obj):
    	return "\n".join([p.var for p in obj.day.all()])
    def get_month(self,obj):
    	return "\n".join([p.var for p in obj.month.all()])
    def get_week(self,obj):
    	return "\n".join([p.var for p in obj.week.all()])	

class ListIP(admin.ModelAdmin):
    list_display=('id','host_ip','describe','get_user')
    def get_user(self,obj):
    	return ", ".join([p.username for p in obj.user.all()])
admin.site.register(Crond,ListCrond)
admin.site.register(Crond_ip,ListIP)
