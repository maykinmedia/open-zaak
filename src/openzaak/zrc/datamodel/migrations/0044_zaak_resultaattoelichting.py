# Generated by Django 2.0.9 on 2019-01-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0043_auto_20181227_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaak',
            name='resultaattoelichting',
            field=models.TextField(blank=True, help_text='Een toelichting op wat het resultaat van de zaak inhoudt.', verbose_name='resultaattoelichting'),
        ),
    ]
