# Generated by Django 3.0.8 on 2022-03-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20220323_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementthree',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='advertisementtwo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
