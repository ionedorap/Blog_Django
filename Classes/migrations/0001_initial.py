# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enquete', models.CharField(max_length=100, verbose_name=b'Enquete')),
                ('data', models.DateField(verbose_name=b'Data da Enquete')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50, verbose_name=b'T\xc3\xadtulo da Postagem')),
                ('postagem', models.TextField(verbose_name=b'Postagem')),
                ('data', models.DateField(verbose_name=b'Data da Postagem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
