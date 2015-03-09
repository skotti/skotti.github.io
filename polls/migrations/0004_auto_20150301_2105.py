# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_blogpost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
