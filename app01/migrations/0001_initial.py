# Generated by Django 2.0.6 on 2018-06-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('publish', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
