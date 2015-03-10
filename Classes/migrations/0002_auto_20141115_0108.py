# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquete',
            name='data',
            field=models.DateTimeField(verbose_name=b'Data da Enquete'),
        ),
        migrations.AlterField(
            model_name='postagem',
            name='data',
            field=models.DateTimeField(verbose_name=b'Data da Postagem'),
        ),
    ]
