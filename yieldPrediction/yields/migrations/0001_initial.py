# Generated by Django 3.2.6 on 2021-09-07 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paddocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_t', models.FloatField()),
                ('date', models.DateField()),
                ('paddock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paddocks.paddock')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
