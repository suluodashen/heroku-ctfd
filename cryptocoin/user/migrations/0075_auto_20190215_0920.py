# Generated by Django 2.1.2 on 2019-02-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0074_auto_20190213_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderedeemer',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sequesansw',
            name='answer',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='transferlogs',
            name='hash',
            field=models.CharField(max_length=150),
        ),
    ]