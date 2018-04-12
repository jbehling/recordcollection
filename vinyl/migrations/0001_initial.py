# Generated by Django 2.0.4 on 2018-04-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('released', models.IntegerField()),
                ('label', models.CharField(max_length=500)),
                ('catalog_number', models.CharField(max_length=100)),
            ],
        ),
    ]
