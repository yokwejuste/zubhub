# Generated by Django 2.2.7 on 2021-03-09 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0036_creatorgroup_members_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creatorgroup',
            name='members_count',
        ),
    ]