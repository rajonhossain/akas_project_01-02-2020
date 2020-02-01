# Generated by Django 2.2 on 2020-02-01 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_auto_20200201_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='stdclassrouting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('time', models.TimeField(max_length=100)),
                ('stdsubjectentry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stdclassrouting', to='projectapp.Stdsubjectentry')),
            ],
        ),
    ]
