# Generated by Django 2.0.6 on 2018-07-16 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0017_zaak_bronorganisatie'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='zaak',
            unique_together={('bronorganisatie', 'zaakidentificatie')},
        ),
    ]
