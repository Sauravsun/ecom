# Generated by Django 3.2.10 on 2023-08-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registertb1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('passw', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='registertb',
        ),
    ]
