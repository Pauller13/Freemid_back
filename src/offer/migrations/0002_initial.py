# Generated by Django 5.1.1 on 2024-10-08 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offer', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offermodel',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='user.clientmodel'),
        ),
        migrations.AddField(
            model_name='offerskillmodel',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.offermodel'),
        ),
        migrations.AddField(
            model_name='proposalmodel',
            name='freelancer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='user.freelancermodel'),
        ),
        migrations.AddField(
            model_name='proposalmodel',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proposals', to='offer.offermodel'),
        ),
        migrations.AddField(
            model_name='offerskillmodel',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.skillmodel'),
        ),
        migrations.AddField(
            model_name='offermodel',
            name='required_skills',
            field=models.ManyToManyField(through='offer.OfferSkillModel', to='offer.skillmodel'),
        ),
        migrations.AlterUniqueTogether(
            name='proposalmodel',
            unique_together={('offer', 'freelancer')},
        ),
    ]
