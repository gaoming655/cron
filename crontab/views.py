# Create your views here.
#coding:utf-8
from django.shortcuts import render_to_response,get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from forms import CrondForm,LoginForm
from django.contrib.auth.models import User
from models import Crond,Crond_ip
from django.db import models
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json
import paramiko
import time

def SSH(hostname,cmd):
    try:
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = hostname,username='root', password='xxxxxxxxx')
        stdin,stdout,stderr=s.exec_command(cmd)
        time.sleep(0.5)
        s.close()
        a=stdout.readlines()
        if a:
            return  True
        else:
            return False
    except:
        return False

def cron_save(Form,request):
    f=Form.save(commit=False)
    f.changed_by = request.user
    f.save()
    return f
    
@login_required(login_url="/")
def cron(request):
    if request.method == 'POST':
        show_list=['min','hour','day','month','week','program','program_ip']
        form = CrondForm(request.user,request.POST)
        mm,hh,dd,MM,ww,pro_gram,pro_ip=[request.POST.get(i) for i in show_list]
        if form.is_valid():
            cron_save(form,request)
            if "/dev/null" not in pro_gram:
                pro_gram="  ".join(pro_gram.split()).strip()+" >/dev/null 2>&1"
            else:
                pro_gram="  ".join(pro_gram.split()).strip()
            gid=Crond.objects.get(program=pro_gram).id
            qip=Crond_ip.objects.get(id=int(pro_ip)).host_ip
            print "ip:%s,id:%s" % (qip,gid)
            stat=SSH(qip,"python /opt/shell/crontab_api_add.py %s" % gid)
            print stat
            if stat:
                return HttpResponse(json.dumps({'code' : '0'}))
            else:
                Crond.objects.filter(id=gid).delete()
                return HttpResponse(json.dumps({'code':'1'}))
        else:
            return HttpResponse(json.dumps({'code':'2','message':{'pro_conn_error':form['pro_conn'].errors,'usage_error':form['usage'].errors,'project_error':form['project'].errors,'program_error': form['program'].errors,'conn_db_error':form['conn_db'].errors,'influence_error':form['influence'].errors}}))
    else:
        form = CrondForm(request.user)
#        name = request.user.username
    return render_to_response('index.html', {'form':form}, context_instance=RequestContext(request))

def help(request):
    return render(request,'help.html',{})

def search(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            in_out = True
        else:
            in_out = False
        form = CrondForm(request.user, request.POST)
        ip = request.POST['program_ip']
        if not ip:
            raise  Http404
        pro=request.POST['project'].strip()
        stat = request.POST['status'].strip()
        con_db = request.POST['conn_db'].strip()
        p_conn = request.POST['pro_conn'].strip()
        pro_gram = "  ".join(request.POST['program'].strip().split())
        if stat == "True":
            stat = True
        else:
            stat = False
        object_cron = Crond.objects.filter(program_ip=ip,status=stat,project__icontains=pro,conn_db__icontains=con_db,program__icontains=pro_gram,pro_conn__icontains=p_conn).order_by("-project")
        return render_to_response('list.html',{'form':object_cron,'status':stat,'ip':ip,'on_off':in_out},context_instance = RequestContext(request))
    else:
        if request.user.is_authenticated():
            form = CrondForm(request.user)
        else:
            form = CrondForm(request.user)
    return render_to_response('search.html',{'form':form},context_instance = RequestContext(request))
def change_status(id,status,request):
    try:
        if status == "true":
            status = True
        elif status == "false":
            status = False
        else:
            return False
        f = Crond.objects.get(id=id)
        f.status=status
        f.return_status=True
        f.changed_by =  request.user
        f.save()
#        Crond.objects.filter(id=id).update(status=ststus)
        return True
    except:
        return False
@login_required(login_url="/")
def add(request):
    if request.method == 'POST':     
        ip = request.POST['ip']
        uid = request.POST['id']
        c_status = request.POST['of_status']
        #判断之前的状态
        if c_status == "true":
            o_status = False
        else:
            o_status = True
        qip=Crond_ip.objects.get(id=int(ip)).host_ip
        if_stat = change_status(uid,c_status,request)
        if if_stat:
            try:
                stat=SSH(qip,"python /opt/shell/crontab_api_add.py %s" % uid)
                if stat:                
                    return HttpResponse(json.dumps({'code': '0'}))
                else:
                    Crond.objects.filter(id=uid).update(return_status=False,status=o_status) ##回滚
                    return HttpResponse(json.dumps({'code':'1'}))
            except:
                Crond.objects.filter(id=uid).update(return_status=False,status=o_status)
                return HttpResponse(json.dumps({'code':'5'}))
        else:
            Crond.objects.filter(id=uid).update(return_status=False,status=o_status)
            return HttpResponse(json.dumps({'code':'6'}))
@login_required(login_url="/")
def edit(request,cid):
    if not cid: 
        raise Http404
    else:
        if request.method == 'POST':
            oid=get_object_or_404(Crond,id=int(cid))
            form=CrondForm(request.user,request.POST,instance=oid)
            if form.is_valid():
                cron_save(form,request)
                qip=Crond_ip.objects.get(id=int(request.POST['program_ip'])).host_ip
                SSH(qip,"python /opt/shell/crontab_api_add.py %s" % cid)
                return HttpResponse("<script>alert('OK');window.location.href='/search';</script>")
        else:
            data=Crond.objects.get(id=int(cid))
            form=CrondForm(request.user,instance=data)
            return render_to_response('edit.html',{'form':form},context_instance=RequestContext(request))
 
def login_views(request):
    if request.method == 'GET':
        forms=LoginForm()
        if request.user.is_authenticated():
            return HttpResponseRedirect('/cron')
        return render(request,'login.html',{'forms':forms})
    elif request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        try:
            uri = url.split('?')[1]
            reurl = uri.split('=')[1]
        except:
            reurl = '/cron/'
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                if user.is_superuser:
                    return HttpResponseRedirect('/history/')
                else:
                    return HttpResponseRedirect(reurl)
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponse("<script>alert('用户名或密码错误');window.location.href='/';</script>")
    else:
        raise Http404
    
def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="/")
def history_list(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            form = Crond.history.order_by('-history_date')[:100]
            return render(request,'history.html',{'forms':form})
        else:
            return HttpResponse("<script>alert('您没有权限');window.location.href='/';</script>")
    else:
        raise Http404