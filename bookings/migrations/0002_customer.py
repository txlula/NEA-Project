# Generated by Django 2.2.7 on 2019-11-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('phone_no', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
    ]