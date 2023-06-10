# Generated by Django 2.1.5 on 2023-04-16 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_name', models.CharField(blank=True, default='', max_length=60)),
                ('State', models.IntegerField(blank=True, default='')),
                ('Campus_ID', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Campus Information',
            },
        ),
    ]