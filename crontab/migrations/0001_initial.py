# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crond_ip'
        db.create_table(u'crontab_crond_ip', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('describe', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'crontab', ['Crond_ip'])

        # Adding M2M table for field user on 'Crond_ip'
        m2m_table_name = db.shorten_name(u'crontab_crond_ip_user')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crond_ip', models.ForeignKey(orm[u'crontab.crond_ip'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crond_ip_id', 'user_id'])

        # Adding model 'HistoricalCrond'
        db.create_table(u'crontab_historicalcrond', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('usage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=254, db_index=True)),
            ('pro_conn', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            (u'program_ip_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('conn_db', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('influence', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 14, 0, 0))),
            ('min', self.gf('django.db.models.fields.CharField')(default='*', max_length=200)),
            ('hour', self.gf('django.db.models.fields.CharField')(default='*', max_length=60)),
            ('day', self.gf('django.db.models.fields.CharField')(default='*', max_length=70)),
            ('month', self.gf('django.db.models.fields.CharField')(default='*', max_length=24)),
            ('week', self.gf('django.db.models.fields.CharField')(default='*', max_length=15)),
            ('status', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('return_status', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            (u'changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'crontab', ['HistoricalCrond'])

        # Adding model 'Crond'
        db.create_table(u'crontab_crond', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('usage', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('program', self.gf('django.db.models.fields.CharField')(unique=True, max_length=254)),
            ('pro_conn', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('program_ip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crontab.Crond_ip'])),
            ('conn_db', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('influence', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 14, 0, 0))),
            ('min', self.gf('django.db.models.fields.CharField')(default='*', max_length=200)),
            ('hour', self.gf('django.db.models.fields.CharField')(default='*', max_length=60)),
            ('day', self.gf('django.db.models.fields.CharField')(default='*', max_length=70)),
            ('month', self.gf('django.db.models.fields.CharField')(default='*', max_length=24)),
            ('week', self.gf('django.db.models.fields.CharField')(default='*', max_length=15)),
            ('status', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('return_status', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('changed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'crontab', ['Crond'])


    def backwards(self, orm):
        # Deleting model 'Crond_ip'
        db.delete_table(u'crontab_crond_ip')

        # Removing M2M table for field user on 'Crond_ip'
        db.delete_table(db.shorten_name(u'crontab_crond_ip_user'))

        # Deleting model 'HistoricalCrond'
        db.delete_table(u'crontab_historicalcrond')

        # Deleting model 'Crond'
        db.delete_table(u'crontab_crond')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crontab.crond': {
            'Meta': {'object_name': 'Crond'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'conn_db': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            'day': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '70'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'influence': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'min': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '200'}),
            'month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '24'}),
            'pro_conn': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'program': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254'}),
            'program_ip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crontab.Crond_ip']"}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'return_status': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'week': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '15'})
        },
        u'crontab.crond_ip': {
            'Meta': {'object_name': 'Crond_ip'},
            'describe': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'host_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'crontab.historicalcrond': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalCrond'},
            u'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'conn_db': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 14, 0, 0)'}),
            'day': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '70'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'hour': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '60'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'influence': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'min': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '200'}),
            'month': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '24'}),
            'pro_conn': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            u'program_ip_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'return_status': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'week': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '15'})
        }
    }

    complete_apps = ['crontab']