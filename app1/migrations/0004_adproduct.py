# Generated by Django 3.2.10 on 2023-08-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_registertb1_registertb'),
    ]

    operations = [
        migrations.CreateModel(
            name='adproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=500)),
                ('modelcolor', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='product/')),
                ('productsize', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
            ],
        ),
    ]
