# Generated by Django 2.2.7 on 2019-11-30 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20191130_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodssku',
            old_name='type',
            new_name='category',
        ),
    ]
