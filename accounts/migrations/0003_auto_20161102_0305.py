# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(serialize=False, max_length=254, primary_key=True)),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, related_name='user_set', verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', blank=True, related_name='user_set', verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Token',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
