# Generated by Django 2.1.2 on 2018-11-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20181104_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='visit_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
