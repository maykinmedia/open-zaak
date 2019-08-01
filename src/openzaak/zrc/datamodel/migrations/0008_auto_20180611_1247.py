# Generated by Django 2.0.6 on 2018-06-11 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0007_zaak_domein_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomeinData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domein_data', models.URLField(help_text='URL naar de domein data resource')),
            ],
            options={
                'verbose_name': 'domeindatareferentie',
                'verbose_name_plural': 'domeindatareferenties',
            },
        ),
        migrations.AlterModelOptions(
            name='zaakobject',
            options={'verbose_name': 'zaakobject', 'verbose_name_plural': 'zaakobjecten'},
        ),
        migrations.RemoveField(
            model_name='zaak',
            name='domein_data',
        ),
        migrations.AddField(
            model_name='domeindata',
            name='zaak',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zrc_datamodel.Zaak'),
        ),
    ]
