# Generated by Django 2.2 on 2020-02-01 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0012_auto_20200201_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdsubjectlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stdsubjectlista', to=settings.AUTH_USER_MODEL),
        ),
    ]
