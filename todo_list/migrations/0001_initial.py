# Generated by Django 2.2.4 on 2019-08-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=40)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
