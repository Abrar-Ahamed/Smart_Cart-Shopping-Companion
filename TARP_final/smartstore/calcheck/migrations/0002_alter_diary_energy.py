# Generated by Django 4.1.7 on 2023-03-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcheck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='energy',
            field=models.IntegerField(null=True),
        ),
    ]