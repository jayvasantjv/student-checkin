# Generated by Django 2.1.5 on 2019-01-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkins', '0005_auto_20190119_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='slot_2',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_3',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_4',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_5',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_6',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_7',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_8',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='slots',
            name='slot_9',
            field=models.CharField(blank=True, choices=[('INFT', 'Information Tech.'), ('CMPN', 'Computer Science'), ('ETRX', 'Electronics'), ('EXTC', 'Electronics & Tele.'), ('BIOM', 'Biomedical'), ('MMS', 'Management Studies')], default=None, max_length=15, null=True),
        ),
    ]
