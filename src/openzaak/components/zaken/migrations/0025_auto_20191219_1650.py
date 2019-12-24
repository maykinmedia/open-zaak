# Generated by Django 2.2.4 on 2019-12-19 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalogi", "0016_auto_20191204_1500"),
        ("zaken", "0024_auto_20191217_1353"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rol", old_name="roltype", new_name="_roltype"
        ),
        migrations.AddField(
            model_name="rol",
            name="_roltype_url",
            field=models.URLField(
                blank=True,
                help_text="URL-referentie naar extern ROLTYPE (in een andere Catalogi API).",
                max_length=1000,
                verbose_name="extern roltype",
            ),
        ),
    ]
