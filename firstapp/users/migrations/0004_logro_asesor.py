# Generated by Django 4.1 on 2022-08-18 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_logro'),
    ]

    operations = [
        migrations.AddField(
            model_name='logro',
            name='asesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.asesor'),
        ),
    ]
