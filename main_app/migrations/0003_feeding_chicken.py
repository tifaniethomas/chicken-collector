# Generated by Django 3.2.12 on 2023-09-13 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='chicken',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main_app.chicken'),
            preserve_default=False,
        ),
    ]
