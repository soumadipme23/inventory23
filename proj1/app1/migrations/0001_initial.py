# Generated by Django 4.1.6 on 2023-05-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('doi', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('vendor', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('vendor', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=100)),
                ('jus', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]