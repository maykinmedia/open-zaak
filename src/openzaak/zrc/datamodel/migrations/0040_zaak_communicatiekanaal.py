# Generated by Django 2.0.9 on 2018-12-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0039_auto_20181224_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaak',
            name='communicatiekanaal',
            field=models.URLField(blank=True, help_text='Het medium waarlangs de aanleiding om een zaak te starten is ontvangen. URL naar een communicatiekanaal in de VNG-Referentielijst van communicatiekanalen.', verbose_name='communicatiekanaal'),
        ),
    ]
