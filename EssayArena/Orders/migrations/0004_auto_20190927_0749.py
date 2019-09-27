# Generated by Django 2.2.5 on 2019-09-27 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Orders', '0003_auto_20190926_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterUniqueTogether(
            name='bid',
            unique_together={('bidder', 'order')},
        ),
    ]
