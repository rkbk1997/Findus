# Generated by Django 3.0.3 on 2020-02-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('pic', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'cate',
            },
        ),
        migrations.CreateModel(
            name='Subcate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofsubcate', models.CharField(max_length=100)),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Cate')),
            ],
            options={
                'db_table': 'subcate',
            },
        ),
    ]
