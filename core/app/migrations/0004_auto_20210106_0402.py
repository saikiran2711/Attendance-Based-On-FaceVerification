# Generated by Django 3.1.2 on 2021-01-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web',
            name='weights',
            field=models.BinaryField(default=None, null=True),
        ),
    ]
