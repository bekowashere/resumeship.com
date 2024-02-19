# Generated by Django 5.0.2 on 2024-02-19 12:42

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48, verbose_name='Plan Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_type', models.IntegerField(choices=[(0, 'Monthly'), (1, 'Yearly ')], default=0, verbose_name='Period Type')),
                ('period_duration', models.PositiveSmallIntegerField(default=30, help_text='The default value is 30 because a month has 30 days. expiry_date = start_date + period_duration', verbose_name='Period Duration')),
                ('start_date', models.DateField(default=datetime.date(2024, 2, 19), verbose_name='Start Date')),
                ('expiry_date', models.DateField(blank=True, null=True, verbose_name='Expiry Date')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Paid Amount')),
                ('is_active', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_subscriptions', to='subscription.plan', verbose_name='Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
