# Generated by Django 3.1 on 2020-08-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
