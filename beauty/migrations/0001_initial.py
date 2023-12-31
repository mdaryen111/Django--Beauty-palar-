# Generated by Django 4.0.4 on 2023-07-23 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_paid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('cost', models.IntegerField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(null=True)),
                ('id_card_on', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.user_status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Apponitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('time1', models.TimeField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.customer')),
                ('paid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.booking_paid')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.servise')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.book_status')),
            ],
        ),
    ]
