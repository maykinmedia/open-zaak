# Generated by Django 2.0.6 on 2018-07-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0023_auto_20180725_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaakobject',
            name='object_type',
            field=models.CharField(choices=[('meldingOpenbareRuimte', 'Melding openbare ruimte')], default='', help_text='Beschrijft het type object gerelateerd aan de zaak', max_length=100),
            preserve_default=False,
        ),
    ]
