# Generated by Django 3.0.3 on 2020-02-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findusapp', '0002_auto_20200229_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
