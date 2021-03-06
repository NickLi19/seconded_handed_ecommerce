# Generated by Django 2.2.7 on 2019-11-18 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='updated time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='deleted marker')),
                ('receiver', models.CharField(max_length=20, verbose_name='receiver')),
                ('addr', models.CharField(max_length=256, verbose_name='address')),
                ('zip_code', models.CharField(max_length=5, null=True, verbose_name='zip_code')),
                ('phone', models.CharField(max_length=10, verbose_name='phone_number')),
                ('is_defualt', models.BooleanField(default=False, verbose_name='is_default_address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'address',
                'db_table': 'df_address',
            },
        ),
    ]
