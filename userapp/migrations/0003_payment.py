# Generated by Django 3.0.3 on 2020-03-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('loc_id', models.IntegerField(blank=True, null=True)),
                ('info', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
