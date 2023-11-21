# Generated by Django 4.2.4 on 2023-10-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('planting_season', models.CharField(max_length=100)),
                ('harvest_season', models.CharField(max_length=100)),
                ('optimal_soil_type', models.CharField(max_length=100)),
                ('optimal_sunlight', models.CharField(max_length=100)),
                ('optimal_temperature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('health_status', models.CharField(max_length=100)),
                ('vaccination_records', models.TextField()),
            ],
        ),
    ]
