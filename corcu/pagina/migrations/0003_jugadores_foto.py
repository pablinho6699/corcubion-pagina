# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_noticias'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='foto',
            field=models.CharField(default='/media/product/no_picture.png', max_length=50),
        ),
    ]
