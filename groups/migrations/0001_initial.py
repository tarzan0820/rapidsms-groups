# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table('groups_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_editable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('groups', ['Group'])

        # Adding M2M table for field contacts on 'Group'
        db.create_table('groups_group_contacts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['groups.group'], null=False)),
            ('contact', models.ForeignKey(orm['rapidsms.Contact'], null=False))
        ))
        db.create_unique('groups_group_contacts', ['group_id', 'contact_id'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table('groups_group')

        # Removing M2M table for field contacts on 'Group'
        db.delete_table('groups_group_contacts')


    models = {
        'groups.group': {
            'Meta': {'object_name': 'Group'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'groups'", 'blank': 'True', 'to': "orm['rapidsms.Contact']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
    }

    complete_apps = ['groups']
