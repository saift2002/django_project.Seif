# Generated by Django 4.0.3 on 2023-06-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fawry', '0006_alter_fawry_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fawry',
            name='profit',
            field=models.CharField(choices=[('كاش', 'كاش'), ('فوري', 'فوري')], max_length=10),
        ),
    ]
