# Generated by Django 5.1.1 on 2024-10-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_project_history_clientmodel_additional_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]