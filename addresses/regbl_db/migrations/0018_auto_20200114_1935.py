# Generated by Django 3.0.2 on 2020-01-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regbl_db', '0017_auto_20200114_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='EDID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addresses',
            name='EGID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='addresses',
            name='GDEKT',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='addresses',
            name='GDENAME',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='addresses',
            name='GDENR',
            field=models.PositiveIntegerField(default=99),
        ),
    ]