# Generated by Django 3.2.4 on 2021-07-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0017_auto_20210710_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librodiario',
            name='debe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='librodiario',
            name='haber',
            field=models.IntegerField(),
        ),
    ]