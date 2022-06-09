# Generated by Django 3.2.8 on 2022-06-08 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hobbifyapp', '0003_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='likee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likes',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
