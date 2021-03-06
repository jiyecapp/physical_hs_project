# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('db_index', models.IntegerField(blank=True, null=True)),
                ('artist', models.TextField(blank=True, null=True)),
                ('attack', models.TextField(blank=True, null=True)),
                ('cardclass', models.TextField(blank=True, db_column='cardClass', null=True)),
                ('classes', models.TextField(blank=True, null=True)),
                ('collectible', models.IntegerField(blank=True, null=True)),
                ('collectiontext', models.TextField(blank=True, db_column='collectionText', null=True)),
                ('cost', models.TextField(blank=True, null=True)),
                ('dbfid', models.TextField(blank=True, db_column='dbfId', null=True)),
                ('durability', models.TextField(blank=True, null=True)),
                ('elite', models.TextField(blank=True, null=True)),
                ('entourage', models.TextField(blank=True, null=True)),
                ('faction', models.TextField(blank=True, null=True)),
                ('flavor', models.TextField(blank=True, null=True)),
                ('health', models.TextField(blank=True, null=True)),
                ('hidestats', models.TextField(blank=True, db_column='hideStats', null=True)),
                ('howtoearn', models.TextField(blank=True, db_column='howToEarn', null=True)),
                ('howtoearngolden', models.TextField(blank=True, db_column='howToEarnGolden', null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('mechanics', models.TextField(blank=True, null=True)),
                ('multiclassgroup', models.TextField(blank=True, db_column='multiClassGroup', null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('overload', models.TextField(blank=True, null=True)),
                ('playrequirements', models.TextField(blank=True, db_column='playRequirements', null=True)),
                ('playerclass', models.TextField(blank=True, db_column='playerClass', null=True)),
                ('race', models.TextField(blank=True, null=True)),
                ('rarity', models.TextField(blank=True, null=True)),
                ('referencedtags', models.TextField(blank=True, db_column='referencedTags', null=True)),
                ('card_set', models.TextField(blank=True, null=True)),
                ('spelldamage', models.TextField(blank=True, db_column='spellDamage', null=True)),
                ('targetingarrowtext', models.TextField(blank=True, db_column='targetingArrowText', null=True)),
                ('card_text', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='CardsZhcn',
            fields=[
                ('db_index', models.IntegerField(blank=True, null=True)),
                ('artist', models.TextField(blank=True, null=True)),
                ('attack', models.TextField(blank=True, null=True)),
                ('cardclass', models.TextField(blank=True, db_column='cardClass', null=True)),
                ('classes', models.TextField(blank=True, null=True)),
                ('collectible', models.IntegerField(blank=True, null=True)),
                ('collectiontext', models.TextField(blank=True, db_column='collectionText', null=True)),
                ('cost', models.TextField(blank=True, null=True)),
                ('dbfid', models.TextField(blank=True, db_column='dbfId', null=True)),
                ('durability', models.TextField(blank=True, null=True)),
                ('elite', models.TextField(blank=True, null=True)),
                ('entourage', models.TextField(blank=True, null=True)),
                ('faction', models.TextField(blank=True, null=True)),
                ('flavor', models.TextField(blank=True, null=True)),
                ('health', models.TextField(blank=True, null=True)),
                ('hidestats', models.TextField(blank=True, db_column='hideStats', null=True)),
                ('howtoearn', models.TextField(blank=True, db_column='howToEarn', null=True)),
                ('howtoearngolden', models.TextField(blank=True, db_column='howToEarnGolden', null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('mechanics', models.TextField(blank=True, null=True)),
                ('multiclassgroup', models.TextField(blank=True, db_column='multiClassGroup', null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('overload', models.TextField(blank=True, null=True)),
                ('playrequirements', models.TextField(blank=True, db_column='playRequirements', null=True)),
                ('playerclass', models.TextField(blank=True, db_column='playerClass', null=True)),
                ('race', models.TextField(blank=True, null=True)),
                ('rarity', models.TextField(blank=True, null=True)),
                ('referencedtags', models.TextField(blank=True, db_column='referencedTags', null=True)),
                ('card_set', models.TextField(blank=True, null=True)),
                ('spelldamage', models.TextField(blank=True, db_column='spellDamage', null=True)),
                ('targetingarrowtext', models.TextField(blank=True, db_column='targetingArrowText', null=True)),
                ('card_text', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'cards_zhCN',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
    ]
