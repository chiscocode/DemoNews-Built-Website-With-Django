# Generated by Django 3.0.8 on 2022-03-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20220323_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=400)),
                ('message', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
