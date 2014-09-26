#coding=utf-8
from django.db import models
import datetime
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Create your models here.
class Crond_ip(models.Model):
    host_ip = models.IPAddressField()
    user = models.ManyToManyField(User)
    describe = models.CharField(max_length=30,blank=True,verbose_name=u'描述')
    def __unicode__(self):
        return u"%s" % (self.host_ip)    

class Crond(models.Model):
    project=models.CharField(max_length=30)
    usage=models.CharField(max_length=100)
    program=models.CharField(max_length=254,unique=True, error_messages={'unique': u'不可以添加重复程序',})
    pro_conn=models.IPAddressField()
    program_ip=models.ForeignKey(Crond_ip)
    conn_db=models.CharField(max_length=20)
    influence=models.CharField(max_length=400)
    date = models.DateField(default=datetime.datetime.now())
    min = models.CharField(max_length=200,default="*")
    hour = models.CharField(max_length=60,default="*")
    day = models.CharField(max_length=70,default="*")
    month = models.CharField(max_length=24,default="*")
    week = models.CharField(max_length=15,default="*")
    status=models.NullBooleanField(default=True)
    return_status=models.NullBooleanField(default=True)
    changed_by = models.ForeignKey(User,null=True,blank=True)
    history = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user_setter(self, value):
        self.changed_by = value

    def __unicode__(self):
        return u"%s   %s" % (self.project,self.date)
