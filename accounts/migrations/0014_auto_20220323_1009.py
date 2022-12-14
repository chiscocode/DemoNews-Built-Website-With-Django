# Generated by Django 3.0.8 on 2022-03-23 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_post_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementone',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='commen', to='accounts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(editable=False, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
