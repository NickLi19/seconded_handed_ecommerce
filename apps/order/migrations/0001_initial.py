# Generated by Django 2.2.7 on 2019-11-19 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_address'),
        ('goods', '0002_auto_20191118_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='updated time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='deleted marker')),
                ('order_id', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='order id')),
                ('pay_method', models.SmallIntegerField(choices=[(1, 'Cash on Delivery'), (2, 'WeChat Pay'), (3, 'AliPay'), (4, 'UniPay'), (5, 'Credit Card')], default=3, verbose_name='payment method')),
                ('total_count', models.IntegerField(default=1, verbose_name='goods amount')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='goods total price')),
                ('transit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='order shipment fee')),
                ('order_status', models.SmallIntegerField(choices=[(1, 'unpaid'), (2, 'undelivered'), (3, 'delivered, waiting for pick up'), (4, 'unevaluated'), (5, 'completed')], default=1, verbose_name='order status')),
                ('trade_no', models.CharField(default='', max_length=128, verbose_name='order number')),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='user.Address', verbose_name='address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'orders',
                'verbose_name_plural': 'orders',
                'db_table': 'df_order_info',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='updated time')),
                ('is_delete', models.BooleanField(default=False, verbose_name='deleted marker')),
                ('count', models.IntegerField(default=1, verbose_name='goods amount')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='goods price')),
                ('comment', models.CharField(default='', max_length=256, verbose_name='comments')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='order.OrderInfo', verbose_name='order')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='goods.GoodsSKU', verbose_name='good_sku')),
            ],
            options={
                'verbose_name': 'order goods',
                'verbose_name_plural': 'order goods',
                'db_table': 'df_order_goods',
            },
        ),
    ]
