# Generated by Django 2.2.12 on 2023-02-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230210_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='requirements',
            field=models.CharField(max_length=100),
        ),
    ]
