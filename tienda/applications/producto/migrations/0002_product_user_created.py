# Generated by Django 3.0.5 on 2021-01-18 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_created',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
