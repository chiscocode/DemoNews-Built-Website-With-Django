# Generated by Django 3.0.8 on 2022-03-20 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220320_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maincomment',
            old_name='posts',
            new_name='post',
        ),
    ]
