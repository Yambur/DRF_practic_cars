# Generated by Django 4.2 on 2024-05-14 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto_milage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milage',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.car'),
        ),
        migrations.AlterField(
            model_name='milage',
            name='moto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='milage', to='vehicle.moto'),
        ),
    ]
