# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(default=datetime.datetime(2018, 2, 10, 1, 36, 10, 151963))),
                ('client_id', models.CharField(max_length=256)),
                ('auth_token', models.CharField(default=b'5ff39e32-1c9d-482b-8d41-ea77ca973850', max_length=512)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=256, null=True)),
                ('last_name', models.CharField(max_length=256, null=True)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('dob', models.DateTimeField(null=True)),
                ('password', models.CharField(max_length=256)),
                ('gender', models.CharField(default=None, max_length=124, choices=[(b'MALE', b'MALE'), (b'FEMALE', b'FEMALE'), (b'OTHER', b'OTHER')])),
                ('profile_pic', models.CharField(max_length=512)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 2, 10, 1, 36, 10, 151394))),
            ],
        ),
        migrations.AddField(
            model_name='loginentry',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
    ]
