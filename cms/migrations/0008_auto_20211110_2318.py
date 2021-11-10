# Generated by Django 3.1.6 on 2021-11-10 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20210630_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='book_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='book_slot',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='history',
            name='doctor_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='doctor_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='patient_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='patient_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='reason',
            field=models.CharField(default='--------', max_length=200),
        ),
    ]
