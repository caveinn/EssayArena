# Generated by Django 2.2.5 on 2019-10-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_client_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]