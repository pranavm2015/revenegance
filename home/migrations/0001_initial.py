# Generated by Django 2.0.6 on 2018-07-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]