# Generated by Django 3.1.5 on 2021-01-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('avg_notice', models.CharField(max_length=200)),
                ('where_use', models.CharField(max_length=200)),
            ],
        ),
    ]
