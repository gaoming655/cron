#coding=utf-8
from django.forms import ModelForm
from crontab.models import Crond,Crond_ip
from django import forms
from django.contrib.auth.models import User
NA_YES_NO = ((True, '启用'), (False, '禁用'))
class CrondForm(ModelForm):
    class Meta:
        model = Crond
        exclude=['date','return_status']
    def __init__(self, user = None, *args, **kwargs):
        self.user = user
        super(CrondForm, self).__init__(*args, **kwargs)
        self.fields['project'].label = u'项目'
        self.fields['usage'].label = u'用途'
        self.fields['program'].label = u'任务'
        self.fields['pro_conn'].label = u'程序连接的IP'
        self.fields['program_ip'].label = u'主机IP(必选)'
        self.fields['conn_db'].label = u'连接的数据库'
        self.fields['influence'].label = u'影响范围'
        self.fields['status'].label=u'查询状态'
        self.fields['min'].label = u'分钟'
        self.fields['hour'].label = u'小时'
        self.fields['day'].label = u'天'
        self.fields['month'].label = u'月份'
        self.fields['week'].label = u'星期'
        self.fields['status'].widget = forms.RadioSelect(choices=NA_YES_NO)
        self.fields['program'].error_messages={'invalid': u'禁止程序重复添加','required':u'任务不能为空'}
        self.fields['project'].error_messages={'required': u'项目不能为空'}
        self.fields['usage'].error_messages={'required': u'用途不能为空'}
        self.fields['influence'].error_messages={'required' : u'影响范围不能为空'}
        self.fields['conn_db'].error_messages={'required': u'连接数据库不能为空'}
        self.fields['pro_conn'].error_messages={'required': u'程序连接IP不能为空','invalid': u'IP地址格式不正确'}
        self.fields['project'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['pro_conn'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['usage'].widget=forms.TextInput(attrs={'class':'form-control',})
        self.fields['program'].widget=forms.TextInput(attrs={'class':'form-control','placeholder':u'请使用命令的全路径，并且URL地址使用双引号'})
        self.fields['conn_db'].widget=forms.TextInput(attrs={'class':'form-control','placeholder': u'请输入数据库的IP地址'})
        self.fields['influence'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['day'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['min'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['hour'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['week'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['month'].widget=forms.TextInput(attrs={'class':'form-control'})
        self.fields['program_ip'].widget=forms.Select(attrs={},choices=self.get_ip_list())
    def get_ip_list(self):
        ip_list=[]
        print self.user
        if not self.user.is_anonymous(): 
            ip = self.user.crond_ip_set.all()
            for i in ip:
                ip_list.append((i.id, i.host_ip))
            return ip_list
        else:
            ip = Crond_ip.objects.all()
            for i in ip:
                ip_list.append((i.id,i.host_ip))
            return ip_list
    def clean_program(self):
        for i in ['rm','reboot','init','shutdown','*']:
            if i in  self.cleaned_data['program']:
                return " "
        if "/dev/null" not in self.cleaned_data['program']:
            self.cleaned_data['program']="  ".join(self.cleaned_data['program'].strip().split())+" >/dev/null 2>&1"
        else:
            self.cleaned_data['program']="  ".join(self.cleaned_data['program'].strip().split())
        return self.cleaned_data['program']
    def clean_project(self):
        self.cleaned_data['project']=self.cleaned_data['project'].strip()
        return self.cleaned_data['project']
    def clean_conn_db(self):
        self.cleaned_data['conn_db']=self.cleaned_data['conn_db'].strip()
        return self.cleaned_data['conn_db']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,label=u"用户名",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(max_length=30,label=u"密码",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'PassWord'}))
