# Generated by Django 2.0.6 on 2018-07-11 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zrc_datamodel', '0015_auto_20180701_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZaakEigenschap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eigenschap', models.URLField(help_text='URL naar de eigenschap in het ZTC')),
                ('waarde', models.TextField()),
                ('zaak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zrc_datamodel.Zaak')),
            ],
            options={
                'verbose_name': 'zaakeigenschap',
                'verbose_name_plural': 'zaakeigenschappen',
            },
        ),
        migrations.RemoveField(
            model_name='domeindata',
            name='zaak',
        ),
        migrations.DeleteModel(
            name='DomeinData',
        ),
    ]
