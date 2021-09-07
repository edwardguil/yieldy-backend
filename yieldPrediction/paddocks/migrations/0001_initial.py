# Generated by Django 3.2.6 on 2021-09-07 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paddock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('size_ha', models.IntegerField()),
                ('rowSpacing_cm', models.FloatField()),
                ('cropParameters', models.CharField(max_length=512)),
                ('postCode', models.IntegerField()),
                ('cropType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crops.crop')),
            ],
        ),
    ]
