# Generated by Django 3.1.2 on 2020-11-01 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorspatients',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_to_doctorsPatients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctorspatients',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_to_doctorsPatients', to=settings.AUTH_USER_MODEL),
        ),
    ]
