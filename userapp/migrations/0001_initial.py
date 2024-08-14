# Generated by Django 5.0 on 2024-02-28 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library_app', '0002_remove_borrow_book_remove_buy_book_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(default=None)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='library_app.product')),
            ],
            options={
                'verbose_name_plural': 'Cart Items',
            },
        ),
        migrations.CreateModel(
            name='User_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='Active')),
                ('address_line1', models.CharField(max_length=100)),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('created_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Address',
            },
        ),
        migrations.CreateModel(
            name='User_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('isactive', models.BooleanField(default=True, verbose_name='Active')),
                ('payment_type', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=50)),
                ('expiry', models.DateTimeField()),
                ('created_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Payment',
            },
        ),
    ]