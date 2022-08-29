# Generated by Django 4.0.3 on 2022-08-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_logro_asesor_logro_asesor_alter_logro_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asesor',
            name='data_created',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
