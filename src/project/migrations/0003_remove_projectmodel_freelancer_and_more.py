# Generated by Django 5.1 on 2024-10-10 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_initial'),
        ('project', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='freelancer',
        ),
        migrations.RemoveField(
            model_name='projectmodel',
            name='offer',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='proposal',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='offer.proposalmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='rating_client',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='rating_freelancer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
