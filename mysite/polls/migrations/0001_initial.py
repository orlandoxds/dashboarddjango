# Generated by Django 3.0.2 on 2020-02-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_breaches',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('domain', models.CharField(blank=True, max_length=100)),
                ('time_breached', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
