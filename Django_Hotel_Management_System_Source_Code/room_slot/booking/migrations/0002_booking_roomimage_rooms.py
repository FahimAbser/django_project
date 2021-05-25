# Generated by Django 3.0.3 on 2020-03-04 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200304_1307'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=5)),
                ('room_type', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('price', models.FloatField(default=1000.0)),
                ('no_of_days_advance', models.IntegerField()),
                ('start_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.RoomManager')),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image', models.ImageField(upload_to='media')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('amount', models.FloatField()),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Rooms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Customer')),
            ],
        ),
    ]
