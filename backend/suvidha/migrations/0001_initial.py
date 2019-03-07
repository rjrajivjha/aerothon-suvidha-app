# Generated by Django 2.1.7 on 2019-03-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msn', models.CharField(max_length=120)),
                ('harness_length', models.TextField()),
                ('gross_weight', models.BooleanField(default=False)),
                ('atmos_pressure', models.IntegerField()),
                ('room_temperature', models.IntegerField()),
                ('airport', models.CharField(max_length=150)),
                ('fuel_capacity_left_wing', models.IntegerField()),
                ('fuel_capacity_right_wing', models.IntegerField()),
                ('fuel_quantity_left_wing', models.IntegerField()),
                ('fuel_quantity_right_wing', models.IntegerField()),
                ('max_altitude_reached', models.IntegerField()),
                ('flight_number', models.CharField(max_length=10)),
            ],
        ),
    ]