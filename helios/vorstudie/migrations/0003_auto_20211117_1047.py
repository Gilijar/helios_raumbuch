# Generated by Django 3.1.13 on 2021-11-17 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0005_auto_20211117_1047'),
        ('vorstudie', '0002_abgabesystem_erzeugungstyp_gebaudenutzung_gewerk_input_investitionskosten_kostenstammdaten_elektro_k'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kostenstammdaten_elektro',
            name='gebaudenutzung',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_elektro',
            name='gewerk',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_elektro',
            name='raumnutzung',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='abgabesystem',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='gebaudenutzung',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='gewerk',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_abgabe',
            name='raumnutzung',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='erzeugungstyp',
        ),
        migrations.RemoveField(
            model_name='kostenstammdaten_hlks_erzeugung',
            name='gewerk',
        ),
        migrations.AddField(
            model_name='input_investitionskosten',
            name='flaeche',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input_investitionskosten',
            name='projekt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projekt.projekt'),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='abgabesystem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.abgabesystem'),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='einheitspreis_pro_m2_elektro',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='einheitspreis_pro_m2_hlks_abgabe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='einheitspreis_pro_m2_hlks_erzeugung',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='gebaudenutzung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gebaudenutzung'),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='gewerk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.gewerk'),
        ),
        migrations.AlterField(
            model_name='input_investitionskosten',
            name='raumnutzung',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projekt.raumnutzung'),
        ),
        migrations.DeleteModel(
            name='Abgabesystem',
        ),
        migrations.DeleteModel(
            name='Erzeugungstyp',
        ),
        migrations.DeleteModel(
            name='Gebaudenutzung',
        ),
        migrations.DeleteModel(
            name='Gewerk',
        ),
        migrations.DeleteModel(
            name='Kostenstammdaten_Elektro',
        ),
        migrations.DeleteModel(
            name='Kostenstammdaten_HLKS_Abgabe',
        ),
        migrations.DeleteModel(
            name='Kostenstammdaten_HLKS_Erzeugung',
        ),
        migrations.DeleteModel(
            name='Raumnutzung',
        ),
    ]
