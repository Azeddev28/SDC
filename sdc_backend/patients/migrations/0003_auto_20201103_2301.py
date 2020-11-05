# Generated by Django 3.1.2 on 2020-11-03 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0002_medicationschedule_medication'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='medicationschedule',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_to_med_sch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_to_meal_plan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='glucoselevelhistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_to_pat_hist', to=settings.AUTH_USER_MODEL),
        ),
    ]