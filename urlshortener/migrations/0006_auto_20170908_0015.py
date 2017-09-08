# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-08 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import urlshortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0005_auto_20170907_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=300, validators=[urlshortener.validators.validate_url, urlshortener.validators.validate_dot_com]),
        ),
    ]
