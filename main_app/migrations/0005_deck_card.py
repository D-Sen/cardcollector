# Generated by Django 2.2.12 on 2023-02-09 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20230209_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Card'),
            preserve_default=False,
        ),
    ]
