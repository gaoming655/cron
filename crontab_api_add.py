#!/bin/env python
#made by G.M
#date 2013-11-20
#sed "/^#id30\b/{N;};//d" 123
#coding : utf-8 
import MySQLdb,sys,subprocess,logging
def initlog():
    logger = logging.getLogger()
    hdlr = logging.FileHandler("/opt/shell/log.txt")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.NOTSET)
    return logger
logger=initlog()
name=int(sys.argv[1])
cron_file="/opt/shell/root"
try:
    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",db="crontab",charset="utf8")
    cur=conn.cursor()
    sql="select min,hour,day,month,week,program from crontab_crond where id = %s and status=True"
    a=""
    cur.execute(sql,name)
    T=cur.fetchall()
    if T:
        for row in T:
            a=" ".join(row)
            logger.info("del id %s\n%s" % (name,a))
            logger.info("add id %s\n%s" % (name,a))
            out,error=subprocess.Popen('sed -i "/^#id%s\\b/{N;};//d" %s' % (name,cron_file),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE).communicate()
            out,error=subprocess.Popen('echo \#id%s >> %s  && echo \'%s\' >> %s' % (name,cron_file,a,cron_file),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE).communicate()
    else:
        logger.info("delete id %s" % name)
        out,error=subprocess.Popen('sed -i "/^#id%s\\b/{N;};//d" %s' % (name,cron_file),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE).communicate()
    cur.close()
    conn.close()
    print "ok"
except:
    pass
