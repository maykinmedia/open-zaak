# Generated by Django 2.2.2 on 2019-06-27 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0068_auto_20190627_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='aoa_huisnummer',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='gor_openbare_ruimte_naam',
            field=models.CharField(blank=True, help_text='Een door het bevoegde gemeentelijke orgaan aan een OPENBARE RUIMTE toegekende benaming', max_length=80),
        ),
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='num_identificatie',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='oao_identificatie',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='ogo_locatie_aanduiding',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='terreingebouwdobject',
            name='wpl_woonplaats_naam',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='aoa_huisnummer',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='gor_openbare_ruimte_naam',
            field=models.CharField(blank=True, help_text='Een door het bevoegde gemeentelijke orgaan aan een OPENBARE RUIMTE toegekende benaming', max_length=80),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='locatie_omschrijving',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='oao_identificatie',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='wpl_woonplaats_naam',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='zaakobject',
            name='object',
            field=models.URLField(blank=True, help_text='URL naar de resource die het OBJECT beschrijft.', max_length=1000),
        ),
    ]
