# Generated by Django 3.2.4 on 2021-06-19 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0007_alter_boleta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletadetalle',
            name='id_boleta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle', to='apirest.boleta'),
        ),
    ]
