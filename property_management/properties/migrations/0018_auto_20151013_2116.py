# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20151013_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='manager',
            field=models.ForeignKey(related_name='managers', default=1, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
