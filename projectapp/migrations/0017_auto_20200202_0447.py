# Generated by Django 2.2 on 2020-02-02 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0016_auto_20200201_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdresult',
            name='stdsubjectentry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stdresultd', to='projectapp.Stdsubjectentry'),
        ),
        migrations.AlterField(
            model_name='stdresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stdresultt', to=settings.AUTH_USER_MODEL),
        ),
    ]
