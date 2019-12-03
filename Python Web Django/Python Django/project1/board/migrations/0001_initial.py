# Generated by Django 2.2.5 on 2019-12-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('br_no', models.AutoField(primary_key=True, serialize=False)),
                ('br_title', models.CharField(max_length=100)),
                ('br_content', models.TextField()),
                ('br_writer', models.TextField()),
                ('br_hit', models.IntegerField()),
                ('br_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
