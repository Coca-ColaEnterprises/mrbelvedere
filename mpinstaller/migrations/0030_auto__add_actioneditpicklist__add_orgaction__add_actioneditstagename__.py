# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActionEditPicklist'
        db.create_table(u'mpinstaller_actioneditpicklist', (
            (u'orgaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpinstaller.OrgAction'], unique=True, primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('custom_object', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('custom_field', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mpinstaller', ['ActionEditPicklist'])

        # Adding model 'OrgAction'
        db.create_table(u'mpinstaller_orgaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('force_sandbox', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_intro', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('content_success', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('content_failure', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mpinstaller', ['OrgAction'])

        # Adding model 'ActionEditStageName'
        db.create_table(u'mpinstaller_actioneditstagename', (
            (u'orgaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpinstaller.OrgAction'], unique=True, primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('custom_object', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('custom_field', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('won', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('probability', self.gf('django.db.models.fields.IntegerField')()),
            ('forecast_category', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'mpinstaller', ['ActionEditStageName'])

        # Adding field 'PackageVersionDependency.action'
        db.add_column(u'mpinstaller_packageversiondependency', 'action',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='required_by', null=True, to=orm['mpinstaller.OrgAction']),
                      keep_default=False)


        # Changing field 'PackageVersionDependency.requires'
        db.alter_column(u'mpinstaller_packageversiondependency', 'requires_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['mpinstaller.PackageVersion']))

    def backwards(self, orm):
        # Deleting model 'ActionEditPicklist'
        db.delete_table(u'mpinstaller_actioneditpicklist')

        # Deleting model 'OrgAction'
        db.delete_table(u'mpinstaller_orgaction')

        # Deleting model 'ActionEditStageName'
        db.delete_table(u'mpinstaller_actioneditstagename')

        # Deleting field 'PackageVersionDependency.action'
        db.delete_column(u'mpinstaller_packageversiondependency', 'action_id')


        # Changing field 'PackageVersionDependency.requires'
        db.alter_column(u'mpinstaller_packageversiondependency', 'requires_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mpinstaller.PackageVersion']))

    models = {
        u'mpinstaller.actioneditpicklist': {
            'Meta': {'object_name': 'ActionEditPicklist', '_ormbases': [u'mpinstaller.OrgAction']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'custom_field': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'custom_object': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'orgaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mpinstaller.OrgAction']", 'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mpinstaller.actioneditstagename': {
            'Meta': {'object_name': 'ActionEditStageName', '_ormbases': [u'mpinstaller.OrgAction']},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'custom_field': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'custom_object': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'forecast_category': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'orgaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['mpinstaller.OrgAction']", 'unique': 'True', 'primary_key': 'True'}),
            'probability': ('django.db.models.fields.IntegerField', [], {}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'won': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'mpinstaller.installationerror': {
            'Meta': {'object_name': 'InstallationError'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'errors'", 'null': 'True', 'to': u"orm['mpinstaller.InstallationErrorContent']"}),
            'fallback_content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'errors_fallback'", 'null': 'True', 'to': u"orm['mpinstaller.InstallationErrorContent']"}),
            'hide_from_report': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {})
        },
        u'mpinstaller.installationerrorcontent': {
            'Meta': {'object_name': 'InstallationErrorContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resolution': ('tinymce.models.HTMLField', [], {})
        },
        u'mpinstaller.metadatacondition': {
            'Meta': {'object_name': 'MetadataCondition'},
            'exclude_namespaces': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'no_match': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'search': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mpinstaller.orgaction': {
            'Meta': {'object_name': 'OrgAction'},
            'content_failure': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_intro': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_success': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'force_sandbox': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'mpinstaller.package': {
            'Meta': {'ordering': "['namespace']", 'object_name': 'Package'},
            'content_failure': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_failure_beta': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_intro': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_intro_beta': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_success': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_success_beta': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'current_beta': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_beta'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"}),
            'current_github': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_github'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"}),
            'current_prod': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_prod'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'force_sandbox': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'namespace': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'mpinstaller.packageinstallation': {
            'Meta': {'ordering': "['-created']", 'object_name': 'PackageInstallation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fork': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'git_ref': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_map': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'instance_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'org_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'org_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'installations'", 'to': u"orm['mpinstaller.Package']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'installations'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"})
        },
        u'mpinstaller.packageinstallationsession': {
            'Meta': {'object_name': 'PackageInstallationSession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessions'", 'to': u"orm['mpinstaller.PackageInstallation']"}),
            'metadata': ('django.db.models.fields.TextField', [], {}),
            'oauth': ('django.db.models.fields.TextField', [], {}),
            'org_packages': ('django.db.models.fields.TextField', [], {})
        },
        u'mpinstaller.packageinstallationstep': {
            'Meta': {'ordering': "['-installation__id', 'order']", 'object_name': 'PackageInstallationStep'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'steps'", 'null': 'True', 'to': u"orm['mpinstaller.InstallationError']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'installation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'steps'", 'to': u"orm['mpinstaller.PackageInstallation']"}),
            'log': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'installation_steps'", 'null': 'True', 'to': u"orm['mpinstaller.Package']"}),
            'previous_version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'installation_steps'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"})
        },
        u'mpinstaller.packageversion': {
            'Meta': {'ordering': "['package__namespace', 'number']", 'object_name': 'PackageVersion'},
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'conditions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['mpinstaller.MetadataCondition']", 'null': 'True', 'blank': 'True'}),
            'content_failure': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_intro': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'content_success': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'github_password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'namespace_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'versions'", 'to': u"orm['mpinstaller.Package']"}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'repo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'subfolder': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zip_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'mpinstaller.packageversiondependency': {
            'Meta': {'ordering': "['order']", 'object_name': 'PackageVersionDependency'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'required_by'", 'null': 'True', 'to': u"orm['mpinstaller.OrgAction']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'requires': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'required_by'", 'null': 'True', 'to': u"orm['mpinstaller.PackageVersion']"}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dependencies'", 'to': u"orm['mpinstaller.PackageVersion']"})
        }
    }

    complete_apps = ['mpinstaller']