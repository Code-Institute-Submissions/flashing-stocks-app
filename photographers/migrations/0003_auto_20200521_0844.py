# Generated by Django 2.2.6 on 2020-05-21 08:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographers', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
