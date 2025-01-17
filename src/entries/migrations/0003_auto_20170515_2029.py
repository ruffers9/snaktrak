# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20170515_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodentry',
            name='user',
            field=models.ForeignKey(related_name='food_entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
