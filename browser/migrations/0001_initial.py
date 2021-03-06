# Generated by Django 3.2.4 on 2021-07-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(choices=[('CDN', 'Canada'), ('CHN', 'China'), ('BZL', 'Brazil'), ('ITA', 'Italy'), ('USA', 'USA')], max_length=3)),
                ('sub_region', models.CharField(max_length=100)),
                ('main_type', models.CharField(choices=[('NOOD', 'Noodle'), ('RICE', 'Rice'), ('DUMP', 'Dumpling'), ('BREA', 'Bread'), ('PIEE', 'Pie')], max_length=4)),
                ('recipe_text', models.TextField(blank=True)),
            ],
        ),
    ]
