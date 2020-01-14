# Generated by Django 3.0.2 on 2020-01-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regbl_db', '0010_remove_addresses_egid'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='EDID',
            field=models.IntegerField(default=-99),
        ),
        migrations.AddField(
            model_name='addresses',
            name='EGID',
            field=models.IntegerField(default=-99),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='GKODE',
            field=models.FloatField(default=-99),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='GKODN',
            field=models.FloatField(default=-99),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='PLZ4',
            field=models.IntegerField(default=-99),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='PLZZ',
            field=models.IntegerField(default=-99),
        ),
    ]