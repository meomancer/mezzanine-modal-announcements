# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteAnnouncement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=200)),
                ('deactivate', models.BooleanField(default=False, help_text=b'If checked this modal will not show')),
                ('start_time', models.TimeField(help_text=b'If present the modal will only show after this time', null=True, blank=True)),
                ('end_time', models.TimeField(help_text=b'If present the model will only show before this time', null=True, blank=True)),
                ('start_date', models.DateField(help_text=b'If present the modal will only show on or after this date', null=True, blank=True)),
                ('end_date', models.DateField(help_text=b'If present the modal will only show on or before this date', null=True, blank=True)),
                ('weekdays', models.CharField(help_text=b'The announcement will only show on the selected days of the week, hold ctrl (cmd on a mac) to select more than one.  If blank the announcement will be eligible to show on any day of the week', max_length=14, blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
