# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImportSetting'
        db.create_table(u'simple_import_importsetting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal(u'simple_import', ['ImportSetting'])

        # Adding unique constraint on 'ImportSetting', fields ['user', 'content_type']
        db.create_unique(u'simple_import_importsetting', ['user_id', 'content_type_id'])

        # Adding model 'ColumnMatch'
        db.create_table(u'simple_import_columnmatch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('column_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('import_setting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_import.ImportSetting'])),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('null_on_empty', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('header_position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'simple_import', ['ColumnMatch'])

        # Adding unique constraint on 'ColumnMatch', fields ['column_name', 'import_setting']
        db.create_unique(u'simple_import_columnmatch', ['column_name', 'import_setting_id'])

        # Adding model 'ImportLog'
        db.create_table(u'simple_import_importlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='simple_import_log', to=orm['account.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('import_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('error_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('import_setting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_import.ImportSetting'])),
            ('import_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('update_key', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'simple_import', ['ImportLog'])

        # Adding model 'RelationalMatch'
        db.create_table(u'simple_import_relationalmatch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('import_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_import.ImportLog'])),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('related_field_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'simple_import', ['RelationalMatch'])

        # Adding model 'ImportedObject'
        db.create_table(u'simple_import_importedobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('import_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_import.ImportLog'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal(u'simple_import', ['ImportedObject'])


    def backwards(self, orm):
        # Removing unique constraint on 'ColumnMatch', fields ['column_name', 'import_setting']
        db.delete_unique(u'simple_import_columnmatch', ['column_name', 'import_setting_id'])

        # Removing unique constraint on 'ImportSetting', fields ['user', 'content_type']
        db.delete_unique(u'simple_import_importsetting', ['user_id', 'content_type_id'])

        # Deleting model 'ImportSetting'
        db.delete_table(u'simple_import_importsetting')

        # Deleting model 'ColumnMatch'
        db.delete_table(u'simple_import_columnmatch')

        # Deleting model 'ImportLog'
        db.delete_table(u'simple_import_importlog')

        # Deleting model 'RelationalMatch'
        db.delete_table(u'simple_import_relationalmatch')

        # Deleting model 'ImportedObject'
        db.delete_table(u'simple_import_importedobject')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'auth_items': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_auth_items'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['authorization.AuthItem']"}),
            'avatar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['uploads.Image']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'authorization.authitem': {
            'Meta': {'object_name': 'AuthItem'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'parent'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['authorization.AuthItem']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dep_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simple_import.columnmatch': {
            'Meta': {'unique_together': "(('column_name', 'import_setting'),)", 'object_name': 'ColumnMatch'},
            'column_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'header_position': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_setting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple_import.ImportSetting']"}),
            'null_on_empty': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'simple_import.importedobject': {
            'Meta': {'object_name': 'ImportedObject'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_log': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple_import.ImportLog']"}),
            'object_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'simple_import.importlog': {
            'Meta': {'object_name': 'ImportLog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'import_setting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple_import.ImportSetting']"}),
            'import_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'update_key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'simple_import_log'", 'to': u"orm['account.User']"})
        },
        u'simple_import.importsetting': {
            'Meta': {'unique_together': "(('user', 'content_type'),)", 'object_name': 'ImportSetting'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.User']"})
        },
        u'simple_import.relationalmatch': {
            'Meta': {'object_name': 'RelationalMatch'},
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_log': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple_import.ImportLog']"}),
            'related_field_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'folder_name': ('agona.core.dynamicsites.fields.FolderNameField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subdomains': ('agona.core.dynamicsites.fields.SubdomainListField', [], {'blank': 'True'})
        },
        u'uploads.image': {
            'Meta': {'object_name': 'Image'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.User']"}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'temporary': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['simple_import']