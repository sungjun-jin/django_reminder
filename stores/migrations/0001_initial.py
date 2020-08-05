# Generated by Django 3.0.3 on 2020-08-05 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.Store')),
            ],
            options={
                'db_table': 'menus',
            },
        ),
    ]
